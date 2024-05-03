num1 = float(input("Ingrese el número 1: "))
num2 = float(input("Ingrese el número 2: "))

suma = num1 + num2
resta = num1 - num2
multi = num1 * num2

# Agregamos manejo de división por cero
if num2 != 0:
    div = num1 / num2
else:
    div = "Error: División por cero"

opcion = input("¿Qué operación deseas realizar? suma, resta, multiplicación, división: ")

if opcion == 'suma':
    resultado = suma
elif opcion == 'resta':
    resultado = resta
elif opcion == 'multiplicación':
    resultado = multi
elif opcion == 'división':
    resultado = div
else:
    resultado = "Opción no válida."

print("El resultado es:", resultado)
