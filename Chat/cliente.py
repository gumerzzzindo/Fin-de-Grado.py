import socket
import threading

def receive_messages(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(data.decode())

# Configurar el cliente
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9999))

# Manejar la recepción de mensajes del servidor
receive_thread = threading.Thread(target=receive_messages, args=(client,))
receive_thread.start()

# Enviar mensajes al servidor
while True:
    message = input()
    client.send(message.encode())
