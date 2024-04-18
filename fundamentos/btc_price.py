import requests

def obtener_precio_bitcoin(moneda):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies={moneda}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        precio = data["bitcoin"][moneda]
        return precio
    else:
        print("Error al obtener el precio de Bitcoin.")
        return None

def convertir_bitcoin_a_moneda(bitcoin, moneda):
    precio_moneda = obtener_precio_bitcoin(moneda)
    if precio_moneda:
        conversion = bitcoin * precio_moneda
        return conversion
    else:
        return None

# Ejemplo de uso
bitcoin_cantidad = 1.0  # Cantidad de Bitcoin a convertir
moneda_destino = "usd"  # Moneda a la que se desea convertir (por ejemplo, USD)
conversion = convertir_bitcoin_a_moneda(bitcoin_cantidad, moneda_destino)
if conversion is not None:
    print(f"{bitcoin_cantidad} Bitcoin equivalen a {conversion} {moneda_destino}")
else:
    print("No se pudo realizar la conversión.")
