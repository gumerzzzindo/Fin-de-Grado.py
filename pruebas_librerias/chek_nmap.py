import nmap

def check_nmap():
    try:
        nm = nmap.PortScanner()
        print("Nmap version:", nm.nmap_version())
        print("Nmap available: Yes")
    except Exception as e:
        print(f"Error: {e}")
        print("Nmap available: No")

# Llama a la función para verificar
check_nmap()
