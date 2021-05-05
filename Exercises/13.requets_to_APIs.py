#Create a quizzing game. Make an HTTP request to the Open Trivia API at each
#round of the game to get a new question and present it to the user to answer.
#At the end of each round ask the user if he wants to play again. Keep playing 
#forever until the user types "quit"

#Don't forget to tell if the answer is correct or not at each round and keep the user's score.

import requests

import pprint

import json

print("Bienvenido a Open Trivia")
input("Pulse intro para comenzar el juego")

decision = ""
marcador = 0

while decision != "quit":

    #Hacemos la peticion a la API
    r = requests.get("https://opentdb.com/api.php?amount=1&category=18&difficulty=easy&type=multiple")

    #Imprimimos la respuesta de una forma mas visual
    print(pprint.pprint(r.text))

    #Transformamos el JSON en un diccionario
    pregunta = json.loads(r.text)
    
    print(pregunta['results'][0]['question'])
    print(pregunta['results'][0]['incorrect_answers'][0])
    print(pregunta['results'][0]['incorrect_answers'][1])
    print(pregunta['results'][0]['incorrect_answers'][2])
    print(pregunta['results'][0]['correct_answer'])

    respuesta = input("Introduzca la respuesta correcta:")

    if respuesta == pregunta['results'][0]['correct_answer']:
        marcador += 1
        print("¡Muy bien has acertado!")

    else:
        print("Prueba suerte la próxima vez...")

    print("Tu puntuación es:", marcador)


    decision = input("¿Desea seguir jugando? (Introduzca quit para salir)")