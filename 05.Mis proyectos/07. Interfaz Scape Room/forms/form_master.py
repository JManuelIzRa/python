import tkinter as tk
from tkinter.ttk import Style
from tkinter.font import BOLD
import util.generic as utl
from PIL import ImageTk, Image
class MasterPanel:

    def __init__(self):

        self.ventana = tk.Tk()
        self.ventana.title("Master Panel")
        w,h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()

        self.ventana.geometry("%dx%d+0+0" % (w,h))
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)

        Style().configure("TFrame", bg='#3a7ff6')

        logo = utl.leer_imagen("./imagenes/logo.png", (350,500))
        texto_logo = utl.leer_imagen("./imagenes/logo_pn_texto.png", (300, 300))

        label1 = tk.Label(self.ventana, image=logo)
        label1.place(x=0, y=0, relwidth=0.5, relheight=0.5)

        label2 = tk.Label(self.ventana, image=texto_logo)
        label2.place(x=0, y=510, relwidth=0.5, relheight=0.5)
        

        




        self.ventana.mainloop()