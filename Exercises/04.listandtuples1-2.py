#Create a program that asks the user for his birhtday in the format "DD-MM-YYYY". Then print:
#You were born in [month]

fecha = list(input("Introduzca su fecha de cumpleaños en el siguiente formato: DD-MM-YYYY: "))

print(fecha)

meses = ("January", "February", "March", "April")#Creamos la tupla meses

mescumple = fecha[3] + fecha[4]#Para llamar a la tupla concatenamos las dos cifras que componen el mes

print("You were born in", meses[int(mescumple)-1])#Tenemos que restarle una porque la enumeracion empieza por 0