import random
import string

from tkinter import *

def generar_password():
    
    #Borramos la entrada de datos
    salida.delete(0,END)
    salida2.delete(0,END)
    #Obtenemos el dato de la entrada
    n = int(entrada.get())

    pwd = ""#Aqui guardaremos la contraseña que primero será una cadena vacía

    caracteres = list(string.printable)#string.printable devuelve los caracteres que se pueden mostrar por pantalla, incluyendo simbolos, numeros, etc
    caracteres_def = caracteres[:-6]#Tenemos que quitarle los seis ultimos elementos

    for i in range(n):
        pwd += random.choice(caracteres_def)#escoge y concatena un elemento aleatorio de la lista

    #Insertamos el resultado
    salida.insert(0,pwd)

    
    ################probabilidad teorica de que descubran la contraseña: #########################
    m = len(caracteres)
    p = (1/m)**n

    #Insertamos la probabilidad de ser descubierta
    pr="{:.2e}".format(p)##{}formato exponencial en notacion cientifica y dos decimal

    salida2.insert(0,pr)

def copiar():
    #Limpiamos el clipboard
    root.clipboard_clear()

    #Copiamos al clipboard
    root.clipboard_append(salida.get())

            
if __name__ == '__main__':
    
    #Instanciamos la interfaz
    root = Tk()

    #Establecemos el titulo de la ventana
    root.title('Generador de contraseñas')

    #Establecemos el tamaño
    root.geometry("500x500")

    #Declaramos un frame
    lf = LabelFrame(root, text="Longitud de la contraseña:")

    #Esta sera la situacion dentro del frame
    lf.pack(pady=20)

    #Creamos el frame, a partir de aqui comienzan a mostrarse datos
    #Creamos un cuadro de entrada de datos
    entrada = Entry(lf, font=("Helvetica", 24))
    entrada.pack(pady=20, padx=20)

    #Creamos dos cuadros para la salida de datos
    salida = Entry(root, text='', font=("Helvetica",24), bd=0, bg="systembuttonface")
    salida.pack(pady=20)

    lf2 = LabelFrame(root, text="Probabilidad de que sea descubierta:", bd=0)
    lf2.pack(pady=20)

    salida2 = Entry(lf2, text='', font=("Helvetica",24), bd=0, bg="systembuttonface")
    salida2.pack(pady=20,padx=20)

    #Creamos un frame para los botones
    mi_frame = Frame(root)
    mi_frame.pack(pady=20)

    #Creamos botones
    mi_boton1 = Button(mi_frame, text="Generar contraseña", command=generar_password)
    mi_boton1.grid(row=0, column=0, padx=10)

    boton_de_copia = Button(mi_frame, text="Copiar", command=copiar)
    boton_de_copia.grid(row=0, column=1, padx=10)

    root.mainloop()
