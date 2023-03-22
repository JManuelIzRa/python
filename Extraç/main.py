import requests
from bs4 import BeautifulSoup

url = "https://moodle.uco.es/m2223/login/index.php"

# crear una instancia de Session en lugar de una instancia de Request
session = requests.Session()

# hacer una solicitud GET para obtener el contenido HTML de la página y mantener la sesión activa
response = session.get(url)

# crear un objeto BeautifulSoup para analizar el contenido HTML
soup = BeautifulSoup(response.content, 'html.parser')

# encontrar el elemento logintoken
logintoken_element = soup.find('input', {'name': 'logintoken'})

# obtener el valor del atributo value del elemento logintoken
logintoken_value = logintoken_element.get('value')

# imprimir el valor del logintoken
print('Valor de logintoken:', logintoken_value)

username = 'p82izraj'
password = 'Josemanuel0$s'

# create a dictionary of the parameters to be sent in the POST request
payload = {'anchor':"",'logintoken':logintoken_value, 'username': username, 'password': password}

# send the POST request
response = session.post(url, data=payload)

soup = BeautifulSoup(response.content, 'html.parser')

# verificar si existe un elemento con el id "loginerrormessage" en la página
login_error_message_element = soup.find('a', {'id': 'loginerrormessage'})
if login_error_message_element:
    print('Error de inicio de sesión:', login_error_message_element.text.strip())
else:
    print('No se encontró ningún error de inicio de sesión.')

# print the response content
#print(response.content)