#Create a guess game with the names of the colors. At each round pick a random color from a list and let the user try
#to guess it. When he does it, ask if he wants to play again. Keep playing until the user types "no"

#El enunciado pide que lo cojamos de una lista, pero prefiero hacerlo con tuplas porque así se evitan modificaciones en la información.

import random

colores = ("rojo", "azul", "verde", "amarillo", "negro", "blanco")

decision = input("Desea jugar?: ").lower()

while decision != "no":

    color = colores[random.randint(0,len(colores)-1)]
    print(color)
    while True:

        guess = input("En que color estoy pensando: ").lower()

        if (guess == color):
            break
        else:
            print("Vuelva a intentarlo")
            continue
    
    print("Has acertado")
    decision = input('Desea volver a jugar?: Introduzca "no" para dejar de jugar: ').lower()