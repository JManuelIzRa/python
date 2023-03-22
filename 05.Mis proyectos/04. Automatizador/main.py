from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from bs4 import BeautifulSoup

def Scroll(driver):
    #We make a slow scroll to the end of the page
    iter=1
    while True:
        

        scrollHeight = driver.execute_script("return document.documentElement.scrollHeight")
        Height=250*iter
        driver.execute_script("window.scrollTo(0, " + str(Height) + ");")
        if Height > scrollHeight:
            print('End of page')
            break
        time.sleep(1)
        iter+=1

def ObtenerEnlaces():
    enlaces = []
    #we get the internal html code of the body
    body = driver.execute_script("return document.body")
    source = body.get_attribute('innerHTML')

    soup = BeautifulSoup(source, "html.parser")

    for href in soup.find_all('a',href=True):
        enlaces.append(href.get('href'))

    return enlaces

if __name__ == '__main__':
    
    option = webdriver.ChromeOptions()
    option.add_argument('--user-data-dir=C:\\Users\\José Manuel\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
    
    # Crear una sesión de Firefox
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)

    driver.implicitly_wait(30)
    driver.maximize_window()
    
    # Acceder a la aplicación web
    driver.get("https://www.einforma.com/informes-empresas/CORDOBA/Rambla--La-.html")

    #accept_cookies = driver.find_element(By.ID,'didomi-notice-agree-button')

    #accept_cookies.click()

    enlaces = []
    #Scroll(driver)

    while(True):
        siguienteEnlace = []
        # encontrar el elemento que contiene el enlace "siguiente"
        siguienteEnlace = driver.find_elements(by=By.LINK_TEXT, value="siguiente >")

        if siguienteEnlace:
            siguienteEnlace[0].click()
            #Scroll(driver)

            enlaces.extend(ObtenerEnlaces())

        else:
            break
     

    #print(enlaces)

    driver.get(enlaces[10])

    # encontrar la tabla que contiene los tbody
    tablas = driver.find_elements_by_tag_name("table")

    # obtener todos los elementos tbody de la tabla
    for tabla in tablas:
        tbody_elementos = tabla.find_elements_by_tag_name("tbody")

        for elemento in tbody_elementos:
                contenido_tbody = elemento.text
                print(contenido_tbody)
