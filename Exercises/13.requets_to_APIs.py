#Create a quizzing game. Make an HTTP request to the Open Trivia API at each
#round of the game to get a new question and present it to the user to answer.
#At the end of each round ask the user if he wants to play again. Keep playing 
#forever until the user types "quit"

#Don't forget to tell if the answer is correct or not at each round and keep the user's score.

import requests

import pprint

import json

import random

import html

print("Bienvenido a Open Trivia")
input("Pulse intro para comenzar el juego")

decision = ""
marcador = 0

while decision != "quit":

    #Hacemos la peticion a la API
    r = requests.get("https://opentdb.com/api.php?amount=1&category=18&difficulty=easy&type=multiple")

    #Comprobamos que la solicitus se haya devuelto correctamente
    if (r.status_code != 200):
        decision = input("Ha habido un error obteniendo la petición. Vuelva a intentarlo pulsando enter o introduzca quit para salir:")
    
    else:
    
        #Imprimimos la respuesta de una forma mas visual
        print(pprint.pprint(r.text))

        #Transformamos el JSON en un diccionario
        datos = json.loads(r.text)

        #Guardamos los datos del diccionario en variables
        pregunta = datos['results'][0]['question']
        respuestas = datos['results'][0]['incorrect_answers']
        respuesta_correcta = datos['results'][0]['correct_answer']
        
        respuestas.append(respuesta_correcta)   #Añadimos la respuesta correcta a la lista de respuestas

        random.shuffle(respuestas)  #"Baraja las respuestas"


        print(html.unescape(pregunta) + "\n")   #Para que no se muestren simbolos raros (&quot;....;&quot) se usa el modulo de HTML

        for respuesta in respuestas:
            print(html.unescape(respuesta))

        respuesta_usuario = input("Introduzca la respuesta correcta:")

        if respuesta_usuario.lower() == respuesta_correcta.lower():
            marcador += 1
            print("¡Muy bien has acertado!")

        else:
            print("Prueba suerte la próxima vez...")

        print("Tu puntuación es:", marcador)


        decision = input("¿Desea seguir jugando? (Introduzca quit para salir)")