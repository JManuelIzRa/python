import scapy.all as scapy
from time import time
# Ahora vamos a construir una función que nos ayude a analizar la red wifi a la cual estamos conectados.
def escanear(direccion_ip):
    scapy.arping(direccion_ip)


escanear("192.168.1.1/24")