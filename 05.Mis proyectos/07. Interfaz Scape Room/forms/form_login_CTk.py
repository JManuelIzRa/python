import customtkinter as Ctk
import tkinter as tk
from customtkinter  import CTk, CTkFrame, CTkEntry, CTkLabel,CTkButton,CTkCheckBox, CTkImage
from tkinter import PhotoImage

import util.generic as utl

class App:

    def __init__(self):

        self.ventana = Ctk.CTk()
        self.ventana.title("Inicio de sesion")
        self.ventana.geometry('1920x1080')
        self.ventana.config(bg='#3a7ff6')
        self.ventana.resizable(width=0, height=0)

        utl.centrar_ventana(self.ventana, 1920, 1080)

        ## Logos
        logo = utl.leer_imagen("./imagenes/logo.png", (350,500))
        texto_logo = utl.leer_imagen("./imagenes/logo_pn_texto.png", (300, 300))

        # Frame Logos
        w,h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        
        text_var = tk.StringVar(value="CTkLabel")

        

        frame_logo = CTkFrame(self.ventana, width=300, height=h/2, fg_color="steel blue")
        
        frame_logo.pack(side=Ctk.LEFT, expand=Ctk.YES, fill=Ctk.BOTH)

        # Aniadimos las imagenes al frame
        label1 = CTkLabel(frame_logo, image=logo, text=None)
        label1.place(x=0, y=0, relwidth=1, relheight=0.5)
        label1.configure(text=None)

        label2 = CTkLabel(frame_logo, image=texto_logo, text=None)
        label2.place(x=0, y=510, relwidth=1, relheight=0.5)
        label2.configure(text=None)

        ## Frame para datos de entrada
        frame_form = CTkFrame(self.ventana, width=w/2, height=h/2, fg_color="light sky blue")
        frame_form.pack(side=Ctk.LEFT, expand=Ctk.YES, fill=Ctk.BOTH)
        
        # Titulo del frame
        frame_form_top = CTkFrame(
            frame_form, width=1920/2,height=50, fg_color="#3a7ff6")
        
        frame_form_top.pack(side="top", fill=Ctk.X)

        title = CTkLabel(frame_form_top, text="INICIO DE SESION", font=(
            'Courier New Greek', 30), pady=10, text_color = "black")
        
        title.pack(expand=Ctk.YES, fill=Ctk.BOTH)

        self.ventana.mainloop()

