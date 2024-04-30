import signal
import sys
import time
import psutil
import inquirer
from scapy.all import *
from scapy.layers.inet import IP, TCP

interfaces = psutil.net_if_addrs()

def signal_handler(sig, frame):
    print("Saliendo, has presionado Ctrl + X")
    sys.exit(0)

def filtro_http(packet: Packet):
    if not (TCP in packet and IP in packet):
        return False
    if packet[IP].dport != 80:
        return False
    if packet[TCP].payload is None:
        return False
    return True

def main():
    signal.signal(signal.SIGINT, signal_handler)
    
    pregunta_int = inquirer.List(
        "interface",
        message="Selecciona una interfaz de red",
        choices=list(interfaces.keys())
    )
    interfaz_seleccionada = inquirer.prompt([pregunta_int]).get("interface")
    print("La interfaz seleccionada es: " + interfaz_seleccionada)
    
    # Capturar paquetes HTTP con Scapy
    sniffer_packets_http = AsyncSniffer(iface=interfaz_seleccionada, prn=lambda x: print(x.summary()) if filtro_http(x) else None)
    sniffer_packets_http.start()
    
    while True:
        try:
            time.sleep(1)  # Puedes ajustar el tiempo de espera según sea necesario
        except KeyboardInterrupt:
            print("Deteniendo la captura...")
            sniffer_packets_http.stop()
            break

if __name__ == "__main__":
    main()
