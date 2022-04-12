from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

option = webdriver.ChromeOptions()
option.add_argument('--user-data-dir=C:\\Users\\José Manuel\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
# Crear una sesión de Firefox
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
driver.implicitly_wait(30)
driver.maximize_window()
# Acceder a la aplicación web
driver.get("https://free-mp3-download.net/")


wait = WebDriverWait(driver, 20)

wait.until(EC.visibility_of_element_located((By.ID, "search")))

# Localizar cuadro de texto
search_field = driver.find_element(By.ID,'q')

# Indicar y confirmar término de búsqueda
argumento_de_busqueda = "Maluma Hawai"
search_field.send_keys(argumento_de_busqueda)


send_button = driver.find_element(By.ID,'snd').click()

# Obtener la lista de resultados de la búsqueda y mostrarla
# mediante el método find_elements_by_class_name
wait.until(EC.visibility_of_element_located((By.ID, "results_t")))

results = driver.find_element(By.ID,'results')

time.sleep(0.9)

driver.find_element(By.XPATH, ("//table/tbody/tr[1]/td[3]/a/button")).click()

wait.until(EC.visibility_of_element_located((By.ID, "song-title")))

time.sleep(20)

driver.find_element(By.XPATH, "//button[contains(text(),'Download')]").click()

time.sleep(3)

# Cerrar la ventana del navegador
#driver.quit()


#jQuery31006134360547240121_1649514250969({"id":1712868197,"readable":true,"title":"Steack H","title_short":"Steack H","title_version":"","isrc":"FRDKW2200078","link":"https:\/\/www.deezer.com\/track\/1712868197","share":"https:\/\/www.deezer.com\/track\/1712868197?utm_source=deezer&utm_content=track-1712868197&utm_term=0_1649514071&utm_medium=web","duration":45,"track_position":78,"disk_number":1,"rank":100000,"release_date":"2022-04-04","explicit_lyrics":true,"explicit_content_lyrics":1,"explicit_content_cover":2,"preview":"https:\/\/cdns-preview-8.dzcdn.net\/stream\/c-8a297398ce3c21da66cf44d3e9aaf8bd-2.mp3","bpm":0,"gain":-14.1,"available_countries":["AE","AF","AG","AI","AL","AM","AO","AQ","AR","AS","AT","AU","AZ","BA","BB","BD","BE","BF","BG","BH","BI","BJ","BN","BO","BQ","BR","BT","BV","BW","BY","CA","CC","CD","CF","CG","CH","CI","CK","CL","CM","CN","CO","CR","CU","CV","CW","CX","CY","CZ","DE","DJ","DK","DM","DO","DZ","EC","EE","EG","EH","ER","ES","ET","FI","FJ","FK","FM","FR","GA","GB","GD","GE","GH","GM","GN","GQ","GR","GS","GT","GU","GW","HK","HM","HN","HR","HU","ID","IE","IL","IN","IO","IQ","IR","IS","IT","JM","JO","JP","KE","KG","KH","KI","KM","KN","KP","KR","KW","KY","KZ","LA","LB","LC","LK","LR","LS","LT","LU","LV","LY","MA","MD","ME","MG","MH","MK","ML","MM","MN","MP","MR","MS","MT","MU","MV","MW","MX","MY","MZ","NA","NE","NF","NG","NI","NL","NO","NP","NR","NU","NZ","OM","PA","PE","PG","PH","PK","PL","PN","PS","PT","PW","PY","QA","RO","RS","RU","RW","SA","SB","SC","SD","SE","SG","SI","SJ","SK","SL","SN","SO","SS","ST","SV","SX","SY","SZ","TC","TD","TG","TH","TJ","TK","TL","TM","TN","TO","TR","TV","TW","TZ","UA","UG","UM","US","UY","UZ","VC","VE","VG","VI","VN","VU","WS","YE","ZA","ZM","ZW"],"contributors":[{"id":9708454,"name":"Rules1492","link":"https:\/\/www.deezer.com\/artist\/9708454","share":"https:\/\/www.deezer.com\/artist\/9708454?utm_source=deezer&utm_content=artist-9708454&utm_term=0_1649514071&utm_medium=web","picture":"https:\/\/api.deezer.com\/artist\/9708454\/image","picture_small":"https:\/\/e-cdns-images.dzcdn.net\/images\/artist\/c69d08d5562fcc5f0220f77d2a8b729a\/56x56-000000-80-0-0.jpg","picture_medium":"https:\/\/e-cdns-images.dzcdn.net\/images\/artist\/c69d08d5562fcc5f0220f77d2a8b729a\/250x250-000000-80-0-0.jpg","picture_big":"https:\/\/e-cdns-images.dzcdn.net\/images\/artist\/c69d08d5562fcc5f0220f77d2a8b729a\/500x500-000000-80-0-0.jpg","picture_xl":"https:\/\/e-cdns-images.dzcdn.net\/images\/artist\/c69d08d5562fcc5f0220f77d2a8b729a\/1000x1000-000000-80-0-0.jpg","radio":true,"tracklist":"https:\/\/api.deezer.com\/artist\/9708454\/top?limit=50","type":"artist","role":"Main"}],"md5_image":"8ed42c7a65d83eda2501b45fea862fae","artist":{"id":9708454,"name":"Rules1492","link":"https:\/\/www.deezer.com\/artist\/9708454","share":"https:\/\/www.deezer.com\/artist\/9708454?utm_source=deezer&utm_content=artist-9708454&utm_term=0_1649514071&utm_medium=web","picture":"https:\/\/api.deezer.com\/artist\/9708454\/image","picture_small":"https:\/\/e-cdns-images.dzcdn.net\/images\/artist\/c69d08d5562fcc5f0220f77d2a8b729a\/56x56-000000-80-0-0.jpg","picture_medium":"https:\/\/e-cdns-images.dzcdn.net\/images\/artist\/c69d08d5562fcc5f0220f77d2a8b729a\/250x250-000000-80-0-0.jpg","picture_big":"https:\/\/e-cdns-images.dzcdn.net\/images\/artist\/c69d08d5562fcc5f0220f77d2a8b729a\/500x500-000000-80-0-0.jpg","picture_xl":"https:\/\/e-cdns-images.dzcdn.net\/images\/artist\/c69d08d5562fcc5f0220f77d2a8b729a\/1000x1000-000000-80-0-0.jpg","radio":true,"tracklist":"https:\/\/api.deezer.com\/artist\/9708454\/top?limit=50","type":"artist"},"album":{"id":309315137,"title":"Techno Dance Mix","link":"https:\/\/www.deezer.com\/album\/309315137","cover":"https:\/\/api.deezer.com\/album\/309315137\/image","cover_small":"https:\/\/e-cdns-images.dzcdn.net\/images\/cover\/8ed42c7a65d83eda2501b45fea862fae\/56x56-000000-80-0-0.jpg","cover_medium":"https:\/\/e-cdns-images.dzcdn.net\/images\/cover\/8ed42c7a65d83eda2501b45fea862fae\/250x250-000000-80-0-0.jpg","cover_big":"https:\/\/e-cdns-images.dzcdn.net\/images\/cover\/8ed42c7a65d83eda2501b45fea862fae\/500x500-000000-80-0-0.jpg","cover_xl":"https:\/\/e-cdns-images.dzcdn.net\/images\/cover\/8ed42c7a65d83eda2501b45fea862fae\/1000x1000-000000-80-0-0.jpg","md5_image":"8ed42c7a65d83eda2501b45fea862fae","release_date":"2022-04-04","tracklist":"https:\/\/api.deezer.com\/album\/309315137\/tracks","type":"album"},"type":"track"})