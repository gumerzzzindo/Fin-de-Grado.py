import signal
import inquirer
from scapy.all import *

# Manejador de la señal SIGINT (Ctrl+C)
def signal_handler(sig, frame):
    print('\nDeteniendo el programa...')
    sys.exit(0)

# Configuración del manejo de la señal SIGINT
signal.signal(signal.SIGINT, signal_handler)

# Diccionario de interfaces de red disponibles
interfaces = {"wlan0": "Interfaz Wi-Fi", "eth0": "Interfaz Ethernet"}

# Pregunta al usuario para seleccionar una interfaz de red
pregunta_int = inquirer.List(
    "interface",
    message="Selecciona una interfaz de red",
    choices=list(interfaces.keys())
)
interfaz_seleccionada = inquirer.prompt([pregunta_int]).get("interface")
print("La interfaz seleccionada es: " + interfaz_seleccionada)

# Función para detectar todos los paquetes ICMP
def detect_icmp(packet):
    if ICMP in packet:
        print("Ping ICMP detectado desde {} hacia {}".format(packet[IP].src, packet[IP].dst))

# Función principal
def main(interface="wlan0"):
    print("Iniciando IDS en la interfaz {}".format(interface))
    sniff(iface=interface, prn=detect_icmp)

# Punto de entrada del programa
if __name__ == "__main__":
    main(interfaz_seleccionada)
