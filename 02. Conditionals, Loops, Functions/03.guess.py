number = 5

guess = int(input("Estoy pensando en un numero, lo adivinas?: "))


while True:
    if (guess == number):
        break
    else:
        guess = int(input("Incorrecto, vuelve a intentarlo: "))

print("Has acertado, el numero era el",number)


#########################################################

#Mismo programa usando random

import random

number = random.randint(0,10) #Random entre 0 y 10