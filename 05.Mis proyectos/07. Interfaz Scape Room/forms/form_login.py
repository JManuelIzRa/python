import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl

from forms.form_master import MasterPanel

class App:

    def __init__(self):

        self.ventana = tk.Tk()
        self.ventana.title("Inicio de sesion")
        self.ventana.geometry('1920x1080')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)

        utl.centrar_ventana(self.ventana, 1920, 1080)

        ## Logos
        logo = utl.leer_imagen("./imagenes/logo.png", (350,500))
        texto_logo = utl.leer_imagen("./imagenes/logo_pn_texto.png", (300, 300))

        # Frame Logos
        w,h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()

        frame_logo = tk.Frame(self.ventana, padx=5, pady=5, bd=0, width=300, height=h/2, bg='#3a7ff6')
        
        frame_logo.pack(side=tk.LEFT, expand=tk.YES, fill=tk.BOTH)

        # Aniadimos las imagenes al frame
        label1 = tk.Label(frame_logo, image=logo)
        label1.place(x=0, y=0, relwidth=1, relheight=0.5)

        label2 = tk.Label(frame_logo, image=texto_logo)
        label2.place(x=0, y=510, relwidth=1, relheight=0.5)

        ## Frame para datos de entrada
        frame_form = tk.Frame(self.ventana, bd=0, width=w/2, height=h/2,
                              relief=tk.SOLID, bg='#3a7ff6')
        frame_form.pack(side=tk.LEFT, expand=tk.YES, fill=tk.BOTH)
        
        # Titulo del frame
        frame_form_top = tk.Frame(
            frame_form, width=1920/2,height=50, bd=0, relief=tk.SOLID, bg='#3a7ff6')
        
        frame_form_top.pack(side="top", fill=tk.X)

        title = tk.Label(frame_form_top, text="Inicio de sesion", font=(
            'Times', 30), bg='#3a7ff6')
        
        title.pack(expand=tk.YES, fill=tk.BOTH)

        self.ventana.mainloop()

