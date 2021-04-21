#Create a program that asks the user for 8 names of people and store them in a list. When all
#names have been given, pìck a random one and print it.

import random

people = []

while len(people) < 8:
    
    person = input("Introduzca un nombre: ")
    people.append(person)

print(people[random.randint(0,7)])

###########################################
#OTRA RESOLUCION

for x in range(0,8):
    person = input("Introduzca un nombre: ")
    people.append(person)