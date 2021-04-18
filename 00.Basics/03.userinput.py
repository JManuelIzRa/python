number1=input("Please enter the first number: ")

print(number1)

number2=input("Please enter the second number: ")

print(number2)

print(number1+number2)#Nos da 48 porque cada vez que llamamos al user input el valor devuelto es un string, entonces lo que realmente estamos haciendo es concatenar number1 y number2

print(float(number1) + float(number2))#Hacemos un casting a float para que se haga la suma correctamente

print(type(number1))#Devuelve el tipo de la variable pasada como argumento

first_name="JoseManuel"
last_name="Iz"

print("Your e-mail addess is",first_name+"."+last_name+"@gmail.com")

#Para que directamente se guarde un tipo distinto a str hacemos lo siguiente:

number1= float(input("Please enter the first number: "))

print(number1)

number2= float(input("Please enter the second number: "))

print(number2)

print(number1+number2)