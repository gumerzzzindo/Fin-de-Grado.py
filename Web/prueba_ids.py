import re
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer

# Configurar el registro de alertas
logging.basicConfig(level=logging.INFO, filename='ids.log', format='%(asctime)s - %(levelname)s - %(message)s')

# Definir patrones de actividad sospechosa
patrones_sospechosos = [
    r'\b(SELECT|INSERT|UPDATE|DELETE)\b',  # Detectar consultas SQL peligrosas
    r'\b(<script>|alert\()\\b'  # Detectar intentos de XSS (Cross-Site Scripting)
]

class IDSHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Verificar si hay patrones sospechosos en la URL
        for patron in patrones_sospechosos:
            if re.search(patron, self.path):
                logging.warning(f"Se ha detectado un patrón sospechoso en la URL: {self.path}")
                print(f"Se ha detectado un patrón sospechoso en la URL: {self.path}")
                break

        self.wfile.write(b'<html><body><h1>Hello World!</h1></body></html>')

# Configurar y ejecutar el servidor web con el manejador IDS
if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, IDSHandler)
    print('Iniciando servidor IDS en el puerto 8000...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
