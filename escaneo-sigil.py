import nmap

def scan_ports(target):
    # Crear un objeto de escaneo Nmap
    nm = nmap.PortScanner()
    
    # Opciones para un escaneo más sigiloso
    arguments = '-sS -T4 -Pn -n --min-rate=1000 --max-retries=2'

    # Realizar el escaneo SYN
    nm.scan(hosts=target, arguments=arguments)

    # Obtener los resultados del escaneo
    for host in nm.all_hosts():
        print(f"Host: {host}")
        for proto in nm[host].all_protocols():
            print(f"Protocolo: {proto}")
            ports = nm[host][proto].keys()
            sorted_ports = sorted(ports)
            for port in sorted_ports:
                state = nm[host][proto][port]['state']
                print(f"Puerto: {port}\tEstado: {state}")

if __name__ == "__main__":
    target = input("Ingresa la dirección IP o el rango de IP a escanear: ")
    scan_ports(target)
