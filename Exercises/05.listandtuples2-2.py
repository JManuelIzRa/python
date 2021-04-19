#Create a program with a predefined list of people. Ask the user for his name, add it to the end of the list and print the updated list.

personas = ["Pepito", "Pepita"]

usuario = input("Introduzca su nombre: ")

personas.append(usuario)

print(personas)