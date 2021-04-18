#Create a program that asks the user for a number of kilometers, converts it to Miles and print the result.
#Knowing that one mille equals to 1,609344Km

km = float(input("Introduzca los km: "))

miles = km/1.609344#Cuando es float obligatoriamente hay que poner un punto para separar la parte decimal.

print(km,"km equivalen a",miles,"millas")

#Si queremos redondear el resultado podemos usar la funcion round()

#miles = round(km/1.609344, <numero de decimales>) ó print(km,"km equivalen a",round(miles, <numero de decimales>),"millas")