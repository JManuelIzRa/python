import requests

r = requests.get("https://www.google.com")  #Enviamos la peticion a la dirección

print(r.status_code)    
#HTTP Status Codes
#200 - OK
#403 - Forbidden
#404 - Not found
#500 - Error en el servidor

#Obtenemos información sobre la peticion
print(r.headers)

#Para obtener un dato en concreto
print(r.headers["Date"])

#La respuesta a nuestra peticion
print(r.text)   #Obtenemos el HTML de la pagina
