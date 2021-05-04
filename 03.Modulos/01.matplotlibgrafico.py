import matplotlib.pyplot as plt #pip install matplotlib

x = [1,2,3,4]

y = [1500,1200,1100,1800]

plt.plot(x,y)   #Crea un grafico de ordenadas representando los puntos (x,y)

plt.show()  #Muestra el grafico

#Podemos asignar una leyenda al grafico

legend = ["January","February","March","April"]

plt.xticks(x,legend) #Asignamos a x la leyenda que hemos creado

#Volvemos a crear el grafo y a mostrarlo

plt.plot(x,y)
plt.show()