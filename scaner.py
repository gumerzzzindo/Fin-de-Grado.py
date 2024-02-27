import nmap

def escanear_puertos(ip):
    nm = nmap.PortScanner()
    
    try:
        nm.scan(ip, arguments='-p 1-1024')  # Escaneo de los primeros 1024 puertos
        print(f"Resultados del escaneo para {ip}:")

        for host in nm.all_hosts():
            print(f"Host: {host}")

            for proto in nm[host].all_protocols():
                print(f"Protocolo: {proto}")

                lport = nm[host][proto].keys()
                for port in sorted(lport):
                    print(f"Puerto {port}: Estado {nm[host][proto][port]['state']}")

    except nmap.PortScannerError as e:
        print(f"Error al escanear puertos: {e}")

# Obtener la IP desde el usuario
ip_a_escanear = input("Ingresa la dirección IP a escanear: ")

# Realizar el escaneo de puertos
escanear_puertos(ip_a_escanear)
