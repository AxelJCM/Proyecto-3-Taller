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
##################################################################
about ="""
___________________________________________
Instituto Tecnologico de Costa Rica         
Computer Engineering                        
Taller de programación                      
                                            
Profesor: Alejandro Vargas                  
Interfaz Grafica                            
                                            
Axel Cordero Martinez                       
Mauro                                       
___________________________________________
"""
##################################################################
class venprincipal:
    def __init__(self):
        
        self.venprincipal = Tk()
        self.venprincipal.title('Proyecto 3')
        self.venprincipal.minsize(1100,576)
        self.venprincipal.resizable(width=NO,height=NO)
        self.fondo1=PhotoImage(file=("img/Fondo princ.png"))
        self.lblfondo1 = Label(self.venprincipal,image=self.fondo1).place(x=0,y=0)
          
        TituloLb = Label(self.venprincipal,text="FORMULA E",font=("calibri","50"),fg= "White",bg= "Black")
        TituloLb.place(x = 365, y = 10)
                
        verEscuderias = Button(self.venprincipal,text='Escuderias',command=lambda:self.opencesc(self.venprincipal),width = "15",fg='white',bg='blue', font=('verdana',10))
        verEscuderias.place(x=200,y=150)

        Pilotos = Button(self.venprincipal,text='Ingresar Pilotos',command=lambda:self.openpiloto(self.venprincipal),width = "15",fg='white',bg='blue', font=('verdana',10))
        Pilotos.place(x=200,y=200)

        AboutBtn = Button(self.venprincipal,text='About',command=lambda:self.openabout(),width = "15",fg='white',bg='blue', font=('verdana',10))
        AboutBtn.place(x=200,y=250)

        TestBtn = Button(self.venprincipal,text="Test Drive",command=lambda:self.TestDrive(self.venprincipal),width = "15",fg='white',bg='blue', font=('verdana',10))
        TestBtn.place(x=200,y=300)

        salirBtn = Button(self.venprincipal,text="SALIR",command=lambda:self.salir(self.venprincipal),fg="red",bg= "white", font=('verdana',10))
        salirBtn.place(x= 240,y= 450)

        
    def openpiloto(self,venprincipal):
        VenPilotos(self.venprincipal)

    def openabout(self):
        VenAbout(self.venprincipal)

    def opencesc(self,venprincipal):
        Escuderias(self.venprincipal)

    def TestDrive(self, venprincipal):
        TestWin(self.venprincipal)

    def salir(self, venprincipal):
        venprincipal.destroy()

    def setMainloop(self):
        self.venprincipal.mainloop()

class VenAbout:
    
    def __init__(self,venprincipal):
        self.venabout=Toplevel()
        venprincipal.withdraw()
        self.venabout.title('About')
        self.venabout.minsize(338,338)
        self.venabout.resizable(width=NO,height=NO)

        self.fondo3= PhotoImage(file=("img/backgroundabout.png"))
        self.lblfondo3 = Label(self.venabout,image=self.fondo3).place(x=0,y=0)
        
        self.L_titulo= Label(self.lblfondo3,text=about,font=('Agency FB',14),fg='black')
        self.L_titulo.pack()

        salirBtn = Button(self.venabout,text="SALIR",command=lambda:salir(self.venabout,venprincipal),fg="red",bg= "Grey")
        salirBtn.place(x=360,y=500)

    def salir(self, venabout,venprincipal):
        venprincipal.deiconify()
        venabout.destroy()
        venprincipal.deiconify

class Escuderias:

    def __init__(self,venprincipal):
        self.escuderias=Toplevel()
        venprincipal.withdraw()
        self.escuderias.title('Escuderias')
        self.escuderias.minsize(877,600)
        self.escuderias.resizable(width=NO,height=NO)
        self.fondo2=PhotoImage(file=("img/ban-1.png"))
        self.lblfondo2 = Label(self.escuderias,image=self.fondo2).place(x=0,y=0)
  
        crearEscuderias = Button(self.escuderias,text='Crear Escuderias',command=lambda:self.openvesc(self.escuderias),fg='white',bg='blue', font=('Agency FB',12))
        crearEscuderias.place(x=100,y=100)
        
    def crear(self):
        self.vencrear=Toplevel()
        self.venprincipal.withdraw()
        self.vencrear.title('Crear Piloto')
        self.vencrear.minsize(1000,700)
        self.vencrear.resizable(width=NO,height=NO)

class VenPilotos:

    def __init__(self,venprincipal):
        self.venpiloto=Toplevel()
        venprincipal.withdraw()
        self.venpiloto.title('Piloto')
        self.venpiloto.minsize(1000,700)
        self.venpiloto.resizable(width=NO,height=NO)

class TestWin:

    def __init__(self,venprincipal):
        self.venTest=Toplevel()
        venprincipal.withdraw()
        self.venTest.title('Test Drive')
        self.venTest.minsize(1000,700)
        self.venTest.resizable(width=NO,height=NO)

    
main = venprincipal() 
main.setMainloop()     
    


#import pickle
#args=["1","2","3","3"]
#def ingresar_datos():
   # print('Ingresar cedula:')
   # ced = input()
   # write(ced)
# Store data (serialize)
#def write(cedula):
    #list_read=read()
    #list_read[cedula]=args
    #with open('filename.pickle', 'wb') as handle:
        #pickle.dump(list_read, handle, protocol=pickle.HIGHEST_PROTOCOL)
# Load data (deserialize)
#def read():
    #with open('filename.pickle', 'rb') as handle:
        #unserialized_data = pickle.load(handle)
    #return unserialized_data

######################################################

#def toggle_entry():
    #global hidden
    #if hidden:
        #e.grid()
    #else:
        #e.grid_remove()
    #hidden = not hidden

#hidden = False
#root = tk.Tk()
#e = tk.Entry(root)
#e.grid(row=0, column=1)
#tk.Button(root, text='Toggle entry', command=toggle_entry).grid(row=0, column=0)
#root.mainloop()

