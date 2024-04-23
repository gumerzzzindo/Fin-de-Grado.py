from scapy.all import *

def packet_callback(packet):
    if packet.haslayer(Dot11):
        if packet.type == 0 and packet.subtype == 8:  # Tipo 0 y Subtipo 8 corresponden al handshake de autenticación de WPA/WPA2
            print("Se ha capturado un handshake de la red:")
            print("BSSID:", packet.addr3)
            print("Cliente:", packet.addr2)
            print("ESSID:", packet.info.decode())

# Configurar la interfaz en modo monitor (solo si es necesario)
# Ejecuta esto en la terminal antes de ejecutar el script:
# sudo airmon-ng start <interfaz>

# Configurar el filtro para capturar solo los paquetes relevantes
sniff(iface="mon0", prn=packet_callback, store=0, filter="type mgt subtype beacon or type mgt subtype assoc-req or type mgt subtype reasso-req or type mgt subtype probe-req or type mgt subtype probe-resp or type ctl subtype assoc-req or type ctl subtype reasso-req")

# Para detener la captura, presiona Ctrl+C
