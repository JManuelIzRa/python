#Create a program to calculate the BMI (body mass index) of a person
#Ask the user for his height in meters and his weight in kg
#BMI = weight / (height^2)

height = float(input("Introduzca su altura en m: "))

weight = float(input("Introduzca su peso en kg: "))

BMI = weight / (height ** 2)

print("Tu BMI es: ", round(BMI, 3))

if (BMI >= 30):
    print("Obesidad")

else:
    if (BMI <= 29.9 and BMI > 24.9):
        print("Sobrepeso")
    
    elif (BMI <= 24.9 and BMI > 18.5):
        print("Peso normal")
    
    else:
        print("Bajo peso")