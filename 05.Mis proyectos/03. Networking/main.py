#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import threading
import ping3 as p
from socket import *
import subprocess
import requests
import json
from time import sleep

#p.EXCEPTIONS = False

def ip_test(ip, actives_ip):

    result = p.ping(ip)
    
    if result != False:
        lock.acquire()
        print("\tActive IP:", ip)
        actives_ip.append(ip)
        lock.release()

def tcp_test(port, target_ip, ports):
	
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.settimeout(10)
        result = sock.connect_ex((target_ip, port))

        if result == 0:
            lock.acquire()
            service = ports[str(port)]
            print(f'\tOpened port {port} {service}')
            lock.release()
    except KeyError:
        lock.acquire()
        print(f'\tOpened port {port}')
        lock.release()
		

def identificar_MAC(mac_address):

    accessToken = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImp0aSI6IjAwZmM3NWY4LTFkYWItNDY4Mi1iY2M3LTIwYWJkNmU3ZWEzYSJ9.eyJpc3MiOiJtYWN2ZW5kb3JzIiwiYXVkIjoibWFjdmVuZG9ycyIsImp0aSI6IjAwZmM3NWY4LTFkYWItNDY4Mi1iY2M3LTIwYWJkNmU3ZWEzYSIsImlhdCI6MTY2NzY0ODQyOSwiZXhwIjoxOTgyMTQ0NDI5LCJzdWIiOiIxMDUxNCIsInR5cCI6ImFjY2VzcyJ9.aDWwsKYV1nztBFnbGQrGK0aZE6IJNmq3q1WbVQy-wJoSrOKCwdmX_c1K0su3DVPGJ64XD8KTpUOu3F434fCf6Q"

    url = "https://api.macvendors.com/v1/lookup/"

    #mac_address = "f4-03-2a-f0-45-53"

    resp = requests.get( url+mac_address,
                    headers = {"Authorization": accessToken}
                )

    respuesta = json.loads(resp.text)

    if not resp.status_code == 200:

        if resp.status_code == 404 and respuesta['errors']['detail'] == "Not Found":
            return "Not Found"
        
        elif resp.status_code == 429:
            print("Status code: {}. Text: {}".format(resp.status_code, resp.text))
            print("The program is gogin to sleep 5 seconds.")
            sleep(5)
            
            resp = requests.get( url+mac_address,
                    headers = {"Authorization": accessToken}
                )

            respuesta = json.loads(resp.text)
        else:
            raise Exception("Incorrect reply from MACVendors API. Status code: {}. Text: {}".format(resp.status_code, resp.text))
    


    return respuesta['data']['organization_name']


if __name__ == '__main__':

    option = 0
    actives_ip = ["192.168.1.1"]

    ports = {"21": "FTP", "22": "SSH","23": "Telnet", "25": "email", "53": "DNS", 
            "80": "HTTP", "443": "HTTPS", "990": "FTPS", "992": "Telnet sobre TLS/SSL",
            "1433": "MS SQL Server", "1521": "Oracle listener", "3306": "MySQL", "3690": "Subversion",
            "5400": "VNC", "5500": "VNC","5600": "VNC","5700": "VNC","5800": "VNC","5900": "VNC", "8000": "iRDMI", "8080": "HTTP alternativo"}

    while option != -1:
        print("Introduzca que desea hacer:")

        option = int(input())

        

        match option:
            case 0:
                print("[-] Escaneo de IP en area local")

                lock = threading.Lock()

                for i in range(2, 255):
                    ip = '192.168.1.%s' %i
                    t =	threading.Thread(target=ip_test, args=(ip, actives_ip))
                    t.start()

                main_thread = threading.current_thread()

                for t in threading.enumerate():
                    if t is not main_thread:
                        t.join()

            case 1:
                print("[-] Escaneo de puertos")

                lock = threading.Lock()

                for target_ip in actives_ip:
                    print("\t[--] Puertos activos para %s", target_ip)

                    for port in ports:
                        t =	threading.Thread(target=tcp_test, args=(int(port), target_ip, ports))
                        t.start()

                    main_thread = threading.current_thread()

                    for t in threading.enumerate():
                        if t is not main_thread:
                            t.join()

            case 2:

                resultado = subprocess.run('arp -a', stdout=subprocess.PIPE)

                cadena = str(resultado.stdout)

                interfaz_internet = cadena[cadena.find("Interfaz: 192.168.1.37"):cadena.find("Interfaz: 192.168.20.1")]

                # Buscamos la posicion inicial donde comienzan los datos
                datos = interfaz_internet[interfaz_internet.find("192.168.1.1"):] 

                datos = datos.split("\\r\\n")

                registro_split = []

                for registro in datos:

                    nuevo_registro = registro.split(" ")

                    registro_split.append(nuevo_registro)

                registro_final = []


                for registro in registro_split:
                    datos_finales = []

                    [datos_finales.append(dato) for dato in registro if dato != '']
                #for dato in registro:
                #    if dato != '':
                #       datos_finales.append(dato)

                    registro_final.append(datos_finales)

                for registro in registro_final:

                    if registro:
                        sleep(0.4)
                        mac_vendor = identificar_MAC(registro[1])

                        registro.append(mac_vendor)

                print("Dirección IP\tDirección MAC\t\tFabricante tarjeta de red")
                print("--------------------------------------------------------------------")

                for registro in registro_final:
                    if registro:
                        print(registro[0]+"\t"+registro[1]+"\t"+registro[3])