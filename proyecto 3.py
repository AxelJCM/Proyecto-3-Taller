#           _____________________________
#__________/BIBLIOTECAS
from tkinter import *               # Tk(), Label, Canvas, Photo
from threading import Thread        # p.start()
import threading
import pickle                       # 
import os                           # ruta = os.path.join('')
import time                         # time.sleep(x)
from tkinter import messagebox      # AskYesNo ()
import tkinter.scrolledtext as tkscrolled
##### Biblioteca para el Carro
from WiFiClient import NodeMCU


class principal:
    def __init__(self):
        
        self.venprincipal=Tk()
        self.venprincipal.title('Proyecto 3')
        self.venprincipal.minsize(1000,700)
        self.venprincipal.resizable(width=NO,height=NO)
        self.fondo1=PhotoImage(file="")
        lblfondo1 = Label(self.venprincipal,image=self.fondo).place(x=0,y=0)

    def botones(self):
        verEscuderias = Button(self.venprincipal,text='Ver Escuderias',command=lambda:(None),fg='white',bg='blue', font=('Agency FB',12))
        verEscuderias.place(x=100,y=100)
        Pilotos = Button(self.venprincipal,text='Ingresar Pilotos',command=lambda:(None),fg='white',bg='blue', font=('Agency FB',12))
        Pilotos.place(x=100,y=100)
        About = Button(self.venprincipal,text='About',command=lambda:(None),fg='white',bg='blue', font=('Agency FB',12))
        About.place(x=100,y=100)
        crearEscuderias = Button(self.venprincipal,text='Crear Escuderias',command=lambda:(None),fg='white',bg='blue', font=('Agency FB',12))
        crearEscuderias.place(x=100,y=100)
    

class VenAbout:

class Escuderias:
    def ver(self):
        
    def crear(self):
        
class VenPilotos:


venprincipal = Tk()
main = VenPrincipal(
venprincipal.mainloop()
    






