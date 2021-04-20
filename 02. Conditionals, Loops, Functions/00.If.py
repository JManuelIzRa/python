num1 = float(input("Introduzca el num1: "))
num2 = float(input("Introduzca el num2: "))

if (num1 > num2):
    #Usando la tabulacion indicamos que está dentro del if
    print(num1, "es mayor que", num2)

elif (num1 == num2):
    print(num1, "es igual que",num2)

else:
    print(num1, "es menor que", num2)

print("Estamos fuera del if")
