#Create a program with a predfefined dictionary for a person. Include the following information: name,
#gender, age, addres and phone

#Ask the user what information he wants to kno about the person (example "name"), then print the value
#associated to that key or display a message in case the key is not found

persona = { "nombre" : "Jose Manuel", "genero" : "Masculino", "edad" : 32, "direccion" : "C/Juan Palomino", "telefono" : 633533433 }

info = input("Que informacion deseas conocer: ").lower() #La funcion lower transforma todo el input a minuscula

print(persona.get(info, "No encontrado"))