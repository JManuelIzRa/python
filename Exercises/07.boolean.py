#Create a program and store your age in a varibale. Then, ask the user for his age and print whether:
#-He's older than you
#-He's younger than you
#-You two have the same age

mi_edad = 20

edad_usr = int(input("Introduzca su edad: "))

if (edad_usr > mi_edad):
    print("El usuario es mayor que yo")

elif(edad_usr < mi_edad):
    print("El usuario es menor que yo")

else:
    print("Tenemos la misma edad")