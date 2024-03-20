#Vamos a tratar de jugar con strigs para crear contraseñas robustas.
#Para ello lo mas seguro es que tengamos que usar la libreria random
import random
import secrets
import string

letras = string.ascii_letters
numeros = string.digits
especial = string.punctuation
seleccion = letras + numeros + especial

long = int(input("Inserta la longitud de caracteres deseada: "))

if long < 8:
    print("Es recomendable que sea mayor o igual a 8 caracteres.")

else:
    contra = ''
for i in range(long):
    contra+= ''.join(secrets.choice(selecion))
    # Imprimios resultado
print(contra)
    
