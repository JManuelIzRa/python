num1 = 5
num2 = 3

print(type(num1))

result = num1/num2

print(type(result))

#Python va cambiando entre tipos de variables

#Para float usamos siempre el punto para separar.

print("Suma",num1 + num2)
print("Resta",num1 - num2)
print("Multiplicacion",num1 * num2)
print("Modulo",5 % 3)
print("Elevado",5 ** 4)
print("Redondeo", round(4.877765389,4))

import math #Importar una libreria matematica

print("Factorial de 5: ",math.factorial(5))#5!
print("Redondeo a la alza: ", math.ceil(2.3))
print("Redondeo a la baja: ",math.floor(2.8))
print("Logaritmo de 20: ", math.log(20))
print("PI: ", math.pi)