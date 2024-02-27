#!/usr/bin/env python3 

num1 = float(input("Ingrese el numero 1: "))
num2 = float(input("Ingrese el numero 2: "))

suma = num1 + num2
resta = num1 - num2
multi = num1 * num2
div = num1 / num2


opcion = input("Que quieres hacer suma, resta, multi, div: ")

if opcion == 'suma':
	resultado = suma
elif opcion == 'resta':
	resultado = resta
elif opcion == 'div':
	resultado = div
elif opcion == 'multi'
	resultado = multi
else:
	print("Opcion no valida.")
exit()
