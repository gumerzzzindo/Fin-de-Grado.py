import secrets
import string
from colorama import Fore, Style

# Definir los conjuntos de caracteres disponibles para la contraseña
letras = string.ascii_letters
numeros = string.digits
especial = string.punctuation
seleccion = letras + numeros + especial

long = int(input(Fore.BLUE+"[?] Inserta la longitud de caracteres deseada: "))

if long < 8:
    print(Fore.RED + "[-] Es recomendable que sea mayor o igual a 8 caracteres.")
    print(Style.RESET_ALL)

else:
    
        
    contra = ''
    for i in range(long):
        contra += ''.join(secrets.choice(seleccion))
        
    # Imprimimos resultado
    if long == 8:
            print(Fore.YELLOW+"Recomendable mayor longitud:", contra)
    else:
        print(Fore.GREEN+"[+] Contraseña generada:", contra)
