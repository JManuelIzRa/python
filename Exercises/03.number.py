#Create a program to calculate the area and circumference of a circle. Ask the user for the radius.
#Knowing that A= pi * r^2 and L = 2 * pi * r

import math #Importamos la libreria matematica

radio = float(input("Introduzca el radio del circulo: "))

area = math.pi * math.pow(radio, 2)

print("El area es: ", round(area,4) )

circunferencia = 2 * math.pi * radio

print("El perimtero o circunferencia es: ", round(circunferencia,4) )