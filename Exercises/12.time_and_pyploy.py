#Create a program to help the user type faster. Give him a word and ask him to write it five times. Check how many seconds it took him to type the word at each round.
#In the end, tell the user how many mistakes were made and show a chart with the typing speed evolution during the 5 rounds

import time as t

from random import randint

import matplotlib.pyplot as plt

diccionario = ("Prueba","Hola, ¿que tal?","¿Como te llamas?")  #Es una tupla ya que nunca será modificado

palabra = diccionario[randint(0,2)]

print("La palabra a escribir es:",palabra)

rondas = [1,2,3,4,5]
resultados = []
errores = 0

input("Presiona enter para comenzar.")

for i in range (0,5):
    
    tiempo_inicial = t.time()

    palabra_usuario = input("Introduzca la palabra:")

    tiempo_final = t.time() - tiempo_inicial

    resultados.append(round(tiempo_final,3))

    if palabra_usuario != palabra:
        errores += 1



print(resultados)
print("Ha cometido",errores,"error(es)")

x = rondas
y = resultados

plt.bar(x,y)

plt.title("Type Test")
plt.ylabel("Tiempo")
plt.xlabel("Ronda")

plt.show()