myString = "Algún texto"

print(type(myString))

myString = "33"

#myString = "She said "meet me at 5"" #Solo reconoce "She said" como cadena

##Si queremos que coja incluso las comillas dobles usaremos comillas simples

myString = 'She said "Meet me at 5"'

print(myString)

##Cada caracter tiene un índice al que podemos acceder con corchetes

print(myString[0])#First character

print(myString[-1])#Last character

print(myString[-2])

print(len(myString))

##Usar lenght para llegar al caracter final

myString = 'She'

print(myString[len(myString)-1])

##Slicing

myString = "ES100002344587"

#Para extraer solo el codigo de pais

print(myString[0 : 2])#El primer numero esta incluido, el segundo no

print(myString[-5:])#Para no tener la limitación del segundo numero

print(myString[:3])#Desde el principio hasta el tercer caracter sin incluirlo 

##Concatenacion

print("Hello" + " " + "World")

#print("Hello" + 1234) Esto da error

print("User"+str(22))
