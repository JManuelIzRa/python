def say_hello(person):

    print("Hello ", person,", how are you?")
    

def fahr2celsius(fahr):
    celsius = (5 * (fahr - 32)) / 9
    return celsius

def people(person1, person2 = "Por defecto"):
    print("Hola",person1,"y",person2)


say_hello("Pepe")

print("Celsius: ",fahr2celsius(100))

print("Kelvin: ",fahr2celsius(100)+273)

people("Pepe")

people("Pepe", "Pepa")