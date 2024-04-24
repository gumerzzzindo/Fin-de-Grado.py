def crear_diccionario(rango_inicio, rango_fin, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        for numero in range(rango_inicio, rango_fin + 1):
            linea = f'{numero:04d}\n'  # Formatea el número con cuatro dígitos, rellenando con ceros a la izquierda si es necesario
            archivo.write(linea)

# Definir el rango que deseas
rango_inicio = 1
rango_fin = 9999
nombre_archivo = 'diccionario.txt'

# Llamar a la función para crear el diccionario
crear_diccionario(rango_inicio, rango_fin, nombre_archivo)

print(f'Se ha creado el diccionario "{nombre_archivo}" con el rango {rango_inicio} - {rango_fin}.')
