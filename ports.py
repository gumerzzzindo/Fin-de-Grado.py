from scapy.all import sniff

interfaz = input("Inserta el nombre de tu interfaz: ")
# Función que se llama por cada paquete capturado
def packet_callback(packet):
    if packet.haslayer("IP") and packet.haslayer("TCP"):
        ip_src = packet["IP"].src
        ip_dst = packet["IP"].dst
        port_src = packet["TCP"].sport
        port_dst = packet["TCP"].dport
        print(f"IP Origen: {ip_src}, Port Origen: {port_src}")
        print(f"IP Destino: {ip_dst}, Puerto Destino: {port_dst}")
        print("----------------------")

# Comienza el sniffing en la interfaz de red especificada

sniff(iface=interfaz, prn=packet_callback, store=0)
