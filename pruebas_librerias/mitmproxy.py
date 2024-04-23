from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    # Captura las solicitudes HTTP antes de que sean enviadas al servidor
    print("Capturando handshake HTTP:")
    print(f"URL: {flow.request.url}")
    print(f"Headers: {flow.request.headers}")
    print(f"Body: {flow.request.text}")

def response(flow: http.HTTPFlow) -> None:
    # Captura las respuestas HTTP antes de que sean enviadas al cliente
    print("Capturando respuesta HTTP:")
    print(f"Status Code: {flow.response.status_code}")
    print(f"Headers: {flow.response.headers}")
    print(f"Body: {flow.response.text}")

# Configurar el servidor proxy mitmproxy
from mitmproxy.tools.main import mitmdump

# Configurar mitmdump para que ejecute nuestro script
addons = [
    # Añadir nuestro script al flujo de mitmdump
    mitmdump.Options
]
# Iniciar mitmdump con nuestros addons
mitmdump(args=["-s", __file__], addons=addons)
