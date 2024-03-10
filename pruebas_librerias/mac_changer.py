import subprocess

interface = input("Inserta el nombre de tu interfaz:")
mac = input("Inserta la MAC deseada:")

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", mac])
subprocess.call(["ifconfig", interface, "up"])
