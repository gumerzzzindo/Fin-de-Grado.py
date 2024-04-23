from bs4 import BeautifulSoup

def detectar_xss(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    if soup.find_all("script"):
        print(f"La URL {url} es vulnerable a Cross-Site Scripting (XSS).")
    else:
        print(f"La URL {url} parece no ser vulnerable a Cross-Site Scripting (XSS).")

# Ejemplo de uso
if __name__ == "__main__":
    url = input("Introduce la URL de la aplicación web para analizar: ")
    detectar_xss(url)
