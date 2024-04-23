import requests

def detectar_sql_injection(url):
    # Intentar inyectar una cadena simple para probar si es vulnerable a SQL injection
    payload = "' OR '1'='1"
    params = {'id': payload}
    response = requests.get(url, params=params)
    if "error" in response.text.lower():
        print(f"La URL {url} es vulnerable a SQL injection.")
    else:
        print(f"La URL {url} parece no ser vulnerable a SQL injection.")

# Ejemplo de uso
if __name__ == "__main__":
    url = input("Introduce la URL de la aplicación web para analizar: ")
    detectar_sql_injection(url)
