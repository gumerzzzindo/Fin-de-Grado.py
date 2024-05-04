from scapy.all import *

def detect_icmp(packet):
    if ICMP in packet:
        print("Ping ICMP detectado desde {} hacia {}".format(packet[IP].src, packet[IP].dst))

def main(interface="wlan0"):
    print("Iniciando IDS en la interfaz {}".format(interface))
    sniff(iface=interface, prn=detect_icmp, filter="icmp")

if __name__ == "__main__":
    main()
