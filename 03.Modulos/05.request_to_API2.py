import requests

import json

API_KEY = ""

id_ciudad = "2519239"

r = requests.get("http://api.openweathermap.org/data/2.5/weather?id=2519239&lang=es&units=metric&appid=")

respuesta = json.loads(r.text)

print(respuesta)

tiempo = respuesta['weather'][0]['description']

temp_actual = respuesta['main']['temp']

sensacion_termica = respuesta['main']['feels_like']

temp_min = respuesta['main']['temp_min']

temp_max = respuesta['main']['temp_max']

humedad = str(respuesta['main']['humidity'])+"%"


print("El timepo hoy sera", tiempo, "Temperatura: ",temp_actual,"T min:",temp_min,"T max:",temp_max,"Sensacion termica:",sensacion_termica,"Humedad:",humedad)
##print(respuesta.text)
