import time as t

print(t.localtime())

time_now  = t.localtime()

print("Transaction completed at", str(time_now.tm_hour) + "h"+ str(time_now.tm_min) + "m")#Podemos usar el . para especificar algunos parámetros en concreto

print(t.time())#Es la cantidad de segundos desde el 1 de Enero de 1970

#El timepo actual y la entrega será en 7 días

time_now = t.time()

delivery_time = time_now + (86400*7)

t.localtime(delivery_time)#Para saber la fecha exacta de la entrega.

t.sleep(5)

