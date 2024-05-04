from scapy.all import *

def detect_ssh(packet):
    if TCP in packet and packet[TCP].dport == 22:
        print("SSH detectado desde {} hacia {}".format(packet[IP].src, packet[IP].dst))

def main(interface="wlan0"):
    print("Iniciando IDS en la interfaz {}".format(interface))
    sniff(iface=interface, prn=detect_ssh, filter="tcp")

if __name__ == "__main__":
    main()
