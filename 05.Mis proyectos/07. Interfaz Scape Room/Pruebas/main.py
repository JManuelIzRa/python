import tkinter
from tkinter import ttk

def saludo():
    print("Hola", nombre.get())

## Ventana principal
root = tkinter.Tk()
root.title("Comisaria 10")
root.geometry("500x300")
nombre = tkinter.StringVar()

## Se incluye un panel para las pestañas
nb = ttk.Notebook(root)
nb.pack(fill="both", expand=True)# Las futuras pestañas llenaran la ventana completamente

## Agrego las pestañas
# Creacion de la pestaña
p1 = ttk.Frame(nb)
p2 = ttk.Frame(nb)
p3 = ttk.Frame(nb)
p4 = ttk.Frame(nb)

# Añadimos la pestaña
nb.add(p1, text='Pestaña1')
nb.add(p2, text='Pestaña2')
nb.add(p3, text='Pestaña3')
nb.add(p4, text='Pestaña4')

## Añadimos elementos a cada una de las pestañas

## Elementos pestaña 1
tkinter.Button(p1, text="saludar", command=saludo).place(x=225, y=160)
tkinter.Entry(p1, textvariable=nombre).place(x=190, y=70)

root.mainloop()