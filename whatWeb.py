import requests
from bs4 import BeautifulSoup
import re

def obtener_titulo(soup):
    title_tag = soup.find('title')
    return title_tag.text.strip() if title_tag else "No se encontró título"

def obtener_version_php(soup):
    version_php = "No se encontró información sobre la versión de PHP"
    scripts = soup.find_all('script')
    for script in scripts:
        if "php" in script.get('src', '').lower():
            match = re.search(r'php(?:-([\d.]+))?.js', script.get('src', ''), re.IGNORECASE)
            if match:
                version_php = match.group(1) if match.group(1) else "Desconocida"
                break
    return version_php

def es_wordpress(soup):
    generator_meta_tag = soup.find('meta', {'name': 'generator'})
    return True if generator_meta_tag and 'wordpress' in generator_meta_tag.get('content', '').lower() else False

def whatweb(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            title = obtener_titulo(soup)
            version_php = obtener_version_php(soup)
            wordpress = "Sí" if es_wordpress(soup) else "No"
            
            print(f"URL: {url}")
            print(f"Título de la página: {title}")
            print(f"Versión de PHP: {version_php}")
            print(f"¿Es WordPress?: {wordpress}")
        else:
            print(f"No se pudo acceder a {url}. Código de estado: {response.status_code}")
    except Exception as e:
        print(f"Error al procesar {url}: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    url = input("Introduce la URL del sitio web a analizar: ")
    whatweb(url)
