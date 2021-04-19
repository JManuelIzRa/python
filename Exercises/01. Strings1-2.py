#Create a program that asks the user for his first name, his middle name and hjis las name. Then print:
#"Your initials are _ _ _"

nombre = input("Introduzca su nombre: ")

apellido1 = input("Introduzca su primer apellido: ")

apellido2 = input("Introduzca su segundo apellido: ")

inicial1 = nombre[0]
inicial2 = apellido1[0]
inicial3 = apellido2[0]

print('"You initials are ' + inicial1 + inicial2 + inicial3 + ' "' )
