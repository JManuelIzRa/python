import requests

import json

import pprint

#Usando quiz API
#Generamos una URL de API

#URL API: https://opentdb.com/api.php?amount=10&category=15&difficulty=easy&type=multiple
#Esta peticion devuelve un JSON

r = requests.get("https://opentdb.com/api.php?amount=10&category=15&difficulty=easy&type=multiple")
print(r.status_code)
print(r.text)

#Working with JSON

questions = json.loads(r.text)

print(questions)

pprint.pprint(questions) #Este modulo lo que hace es mostrar los datos de una forma mas legible

print(questions['results'][0]['category'])


#Transformar una variable a JSON
person = {'Name':'John','Age':30}

person_json = json.dumps(person)

print(person_json)