import scapy.all as scapy

def escaneo(ip):
    scapy.arping(ip)
    
ip = input("[?] Inserta la red/ip que quieras escanear: ")

escaneo(ip)