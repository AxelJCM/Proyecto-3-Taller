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

#==Variables globales==
#diccionario que guarda la información de las ecuderías
escuderias_dict = {}
#diccionario que guarda la información de los pilotos
pilotos_dict = {1:"Juan, Espinoza, 45, Cartago",2:"2",3:"f"}
#diccionario que guarda la información de los patrocinadores
patro_dict = {}
#Contador que cuarda el indice del diccionario de pilotos
esc_cont= 1


class venprincipal:
    def __init__(self):
        global escuderias_dict
        global esc_cont

        if os.stat("contadores.txt").st_size != 0:
            with open ("contadores.txt","rb") as pickle_in: # abre archivo de Pickle para sacar la información guardada
                esc_cont = pickle.load(pickle_in)
            pickle_in.close()

        if os.stat("Pickle.txt").st_size != 0:
            with open ("Pickle.txt","rb") as pickle_in: # abre archivo de Pickle para sacar la información guardada
                escuderias_dict = pickle.load(pickle_in)
            pickle_in.close()
        
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

        Autos = Button(self.venprincipal,text='Automóviles',command=lambda:self.openautos(self.venprincipal),width = "15",fg='white',bg='blue', font=('verdana',10))
        Autos.place(x=200,y=250)

        AboutBtn = Button(self.venprincipal,text='About',command=lambda:self.openabout(self.venprincipal),width = "15",fg='white',bg='blue', font=('verdana',10))
        AboutBtn.place(x=200,y=300)

        TestBtn = Button(self.venprincipal,text="Test Drive",command=lambda:self.TestDrive(self.venprincipal),width = "15",fg='white',bg='blue', font=('verdana',10))
        TestBtn.place(x=200,y=350)

        salirBtn = Button(self.venprincipal,text="SALIR",command=lambda:self.salir(self.venprincipal),fg="red",bg= "white", font=('verdana',10))
        salirBtn.place(x= 240,y= 450)

        
    def openpiloto(self,venprincipal):
        VenPilotos(self.venprincipal)

    def openabout(self,venprincipal):
        VenAbout(self.venprincipal)

    def openautos(self,venprincipal):
        Autos(self.venprincipal)

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
        
        self.L_titulo= Label(self.venabout,text=about,font=('Agency FB',14),fg='black',bg= 'light green')
        self.L_titulo.place(x=18,y=0)

        salirBtn2 = Button(self.venabout,text="Back",font=('Agency FB',16),command=lambda:back1(self.venabout,venprincipal),fg="Orange",bg= "Red")
        salirBtn2.pack(side= BOTTOM)

        def back1(venabout,venprincipal):
            venprincipal.deiconify()
            venabout.destroy()


class Escuderias:

    def __init__(self,venprincipal):
        global escuderias_dict
        global esc_cont
        
        self.escuderias=Toplevel()
        venprincipal.withdraw()
        self.escuderias.title('Escuderias')
        self.escuderias.minsize(877,600)
        self.escuderias.resizable(width=NO,height=NO)
        self.fondo2=PhotoImage(file=("img/ban-1.png"))
        self.lblfondo2 = Label(self.escuderias,image=self.fondo2).place(x=0,y=0)

        if escuderias_dict == {}:
            NothingLb = Label(self.escuderias, text = 'No hay escuderías registradas', font=('calibri',20))
            NothingLb.place(x=280,y=187)

        else:
            print('A',esc_cont)
            TitleLb = Label(self.escuderias, text = '"ESCUDERIAS"', font=('calibri',30))
            TitleLb.place(x=320,y=30)
            
            print(escuderias_dict)
            Baseframe = Frame(self.escuderias,bg='lightblue')
            Baseframe.place(x=100,y=100)

            row_cont = 0
            col_cont = 0
            for i in range(1,esc_cont):
                info = escuderias_dict[i]
                splitInfo = info.split(',')
                print(splitInfo)
                titleLb = Label(Baseframe,text = 'Escuderia' + str(i),font=('calibri',12))
                titleLb.grid(row= row_cont, column = col_cont,ipadx = 3)
                for j in range(0,4):
                    j = Label(Baseframe,text = splitInfo[j],bg='lightblue',font=('calibri',10))
                    j.grid(row= row_cont+1, column = col_cont,ipadx = 10)

                
                    row_cont += 1
                row_cont = 0
                col_cont += 1
            
  
        crearEscuderias = Button(self.escuderias,text='Crear Escuderias',command=lambda:self.CrearEscuderia(),fg='white',bg='blue', font=('Agency FB',12))
        crearEscuderias.place(x=600,y=500)

        SalirBtn = Button(self.escuderias,text="Volver",fg='white',bg='blue',font=('Agency FB',12),command=lambda:self.salir(venprincipal))
        SalirBtn.place(x=100,y=500)

    def salir(self,venprincipal):
        venprincipal.deiconify()
        self.escuderias.destroy()

    def CrearEscuderia(self):
        CrearEscuderia = Crear_Escuderia()


class Crear_Escuderia:

    def __init__(self):
        self.vencrear=Toplevel()
        self.vencrear.title('Crear Escuderia')
        self.vencrear.minsize(1000,700)
        self.vencrear.resizable(width=NO,height=NO)

        NombreEsc = Label(self.vencrear,text='Registrar Nombre',fg='white',bg='blue', font=('Agency FB',12)).place(x=100,y=100)
        self.NameEnt_id = StringVar()
        NameEnt = Entry(self.vencrear,textvariable = self.NameEnt_id,width=50).place(x=300,y=100)

        LogoEsc = Label(self.vencrear,text='Registrar Logo',fg='white',bg='blue', font=('Agency FB',12)).place(x=100,y=200)
        self.LogoEnt_id = StringVar()
        LogoEnt = Entry(self.vencrear,textvariable = self.LogoEnt_id,width=50).place(x=300,y=200)

        UbicacionEsc = Label(self.vencrear,text='Registrar Ubicacion',fg='white',bg='blue', font=('Agency FB',12)).place(x=100,y=300)
        self.UbicacionEnt_id = StringVar()
        UbicacionEnt = Entry(self.vencrear,textvariable = self.UbicacionEnt_id,width=50).place(x=300,y=300)

        PatrocinadorEsc = Label(self.vencrear,text='Registrar Patrocinador',fg='white',bg='blue', font=('Agency FB',12)).place(x=100,y=400)
        self.PatroEnt_id = StringVar()
        PatroEnt = Entry(self.vencrear,textvariable = self.PatroEnt_id,width=50).place(x=300,y=400)

        GuardarEscuderia = Button(self.vencrear,text="Guardar Escuderia",fg='white',bg='blue',font=('Agency FB',12),command=self.save).place(x=300,y=500)

        #SalirBtn = Button(self.escuderias,text="Salir",fg='white',bg='blue',font=('Agency FB',12),command=lambda:self.salir(venprincipal))
        #SalirBtn.place(x=100,y=500)

    #def salir(self,venprincipal):
        #venprincipal.deiconify()
        #self.escuderias.destroy()
        
        
        
    def save(self):
        global escuderias_dict
        global esc_cont
        
        #Guarda los datos en variables
        name = self.NameEnt_id.get()
        logo = self.LogoEnt_id.get()
        Ubic = self.UbicacionEnt_id.get()
        Patro = self.PatroEnt_id.get()
        info = [name,logo,Ubic,Patro] # crea una lista con los datos obtenidos con el fin de facilitar su evaluación
        
        cont = 0 # contador de datos
        for i in info: #ciclo for para evaluar si falta algún dato
            if i == '': #si algun dato no se completó, señala el error
                ErrorLb = Label(self.vencrear,text='*Error. Debe llenar todos los espacios.*',fg='red', font=('calibri',9)).place(x=100,y=50)
                break
            elif cont == 3: # si todos los datos están, los guarda en el diccionario de escuderías
                saved_info =  name + ',' + logo + ',' + Ubic + ',' + Patro
                escuderias_dict.update({esc_cont:saved_info})
            cont+=1 #aumenta en uno el contador de datos

        with open ("contadores.txt","wb") as pickle_out: #Abre archivo de texto de pickle para actualizar las escuderías
            esc_cont += 1
            pickle.dump (esc_cont,pickle_out)
        pickle_out.close()
        
        with open ("Pickle.txt","wb") as pickle_out: #Abre archivo de texto de pickle para actualizar las escuderías
            pickle.dump (escuderias_dict,pickle_out)
        pickle_out.close()
        
        print (escuderias_dict)
        print(esc_cont)
      


class VenPilotos:

    def __init__(self,venprincipal):
        self.venpiloto=Toplevel()
        venprincipal.withdraw()
        self.venpiloto.title('Piloto')
        self.venpiloto.minsize(1000,700)
        self.venpiloto.resizable(width=NO,height=NO)

        RegPilBoton = Button(self.venpiloto,text='Registrar Pilotos',command=lambda:self.RegistrarPilotos(),fg='white',bg='blue', font=('Agency FB',12))
        RegPilBoton.place(x=600,y=500)

    def RegistrarPilotos(self):
        RegistrarPilotos = Registrar_Pilotos()
        RegistrarPilotos.RegPil()

class Registrar_Pilotos:
    
    def __init__(self):
        
        self.venregpiloto=Toplevel()
        self.venregpiloto.title('Registrar Piloto')
        self.venregpiloto.minsize(1000,700)
        self.venregpiloto.resizable(width=NO,height=NO)

    def RegPil(self):

        NombreEsc = Label(self.venregpiloto,text='1)Nombre:',width=13,fg='white',bg='blue', font=('Agency FB',12)).place(x=100,y=100)
        EntradaNombrePil = Entry(self.venregpiloto,width=20).place(x=300,y=100)
        
        EdadPil = Label(self.venregpiloto,text="2)Edad:",width=13,fg='white',bg='blue', font=('Agency FB',12)).place(x=100,y=200)
        EntradaEdadPil = Entry(self.venregpiloto,width=20).place(x=300,y=200)
        
        NacionalidadPil= Label(self.venregpiloto,text="3)Nacionalidad:",width=13,fg='white',bg='blue', font=('Agency FB',12)).place(x=100,y=300)
        EntradaNacionalidadPil = Entry(self.venregpiloto,width=20).place(x=300,y=300)
        
        TemporadaPil = Label(self.venregpiloto,text="4)Temporada:",width=13,fg='white',bg='blue', font=('Agency FB',12)).place(x=100,y=400)
        EntradaTemporadaPil = Entry(self.venregpiloto,width=20).place(x=300,y=400)
        """
        CompetenciasPil = Label(self.venregpiloto,text="5)Cantidad de Competencias:",width=13,fg='white',bg='blue', font=('Agency FB',12)).place(x=100,y=500)

        EntradaCompetenciasPil = Entry(self.venregpiloto,width=20).place(x=300,y=450)

        PartDestPil = Label(self.venregpiloto,text="6)Participacion Destacada:",fg='white',bg='blue', font=('Agency FB',12)).place(x=100,y=600)

        EntradaPartDestPil = Entry(self.venregpiloto,width=20).place(x=300,y=350)

        CompFallPil = Label(self.venregpiloto,text="7)Cantidad Competencias Fallidas:",fg='white',bg='blue', font=('Agency FB',12)).place(x=500,y=100)

        EntradaCompFallPil = Entry(self.venregpiloto,width=20).place(x=700,y=100)

        RGPPil = Label(self.venregpiloto,text="8)RGP:",fg='white',bg='blue', font=('Agency FB',12)).place(x=100,y=400)

        EntradaRGPPil = Entry(self.venregpiloto,width=20).place(x=300,y=350)

        REPPil = Label(self.venregpiloto,text="9)REP:",fg='white',bg='blue', font=('Agency FB',12)).place(x=100,y=400)

        EntradaREPPil = Entry(self.venregpiloto,width=20).place(x=300,y=350)

        IndicePil = Label(self.venregpiloto,text="10)Indice Ganador de Escuderia:",fg='white',bg='blue', font=('Agency FB',12)).place(x=100,y=400)

        EntradaIndicePil = Entry(self.venregpiloto,width=20).place(x=300,y=350)
        """
class Autos:
    pass

class TestWin:

    def __init__(self,venprincipal):
        self.venTest=Toplevel()
        venprincipal.withdraw()
        self.venTest.title('Test Drive')
        self.venTest.minsize(1000,700)
        self.venTest.resizable(width=NO,height=NO)

        StartTestDrive = Button(self.venTest,text='Start Test Drive',command=lambda:self.startTD(self.venTest),fg='white',bg='blue', font=('Agency FB',12))
        crearEscuderias.place(x=600,y=500)

    def startTD(self):
        TestWin(venprincipal)

        


main = venprincipal() 
main.setMainloop()     
    

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

######################################################################
#           ____________________________
#__________/Ventana Principal
"""
root=Tk()
root.title('Proyecto 1')
root.minsize(1000,700)
root.resizable(width=NO,height=NO)
fondo=PhotoImage(file="primerapersona.png")
lblfondo = Label(root,image=fondo).place(x=0,y=0)
    
#Nivel de batería
BatLvl_Btn = Button(root, text= "Nivel de batería: ", fg='white',bg='grey', font=('Agency FB',19), command = lambda:Valor_foto(None))
BatLvl_Btn.place(x=320, y=35)

BatLvl_result = Label(root, text= "Nivel de batería: ", fg='black',bg='white', font=('Agency FB',22))
BatLvl_result.place(x=465, y=40)

#Valor de fotocelda
FotoVal_Btn = Button(root, text= "Valor de fotocelda: ", fg='white',bg='grey', font=('Agency FB',19), command = lambda:Valor_foto(None))
FotoVal_Btn.place(x=640, y=35)

FotoVal_result = Label(root, text= " ", fg='white',bg='black', font=('Agency FB',22))
FotoVal_result.place(x=800, y=40)

#Label de patrones
PatronesLb = Label (root,text='~Patrones:',fg='white',bg='black', font=('Agency FB',22))
PatronesLb.place(x= 140, y= 110)

#Frame de patrones
PatronFrame = Frame(root,bg="black")
PatronFrame.place(x= 155, y= 160)

#botones
BtnWidth = 14

IzquierdaImg = PhotoImage(file = 'FlechaI.png')
TurnLeft = Button(root,image=IzquierdaImg,command=lambda:girarizquierda(None),fg='white',bg='blue', font=('Agency FB',12))
TurnLeft.place(x=270,y=550)

DerechaImg = PhotoImage(file = 'FlechaD.png')
TurnRight = Button(root,image=DerechaImg,command=lambda:girarderecha(None),fg='white',bg='blue', font=('Agency FB',12))
TurnRight.place(x=670,y=550)

AdelanteImg = PhotoImage(file = 'Flecha.png')
MoverAdelante = Button(root,image=AdelanteImg,command=lambda:moveradelante(None),fg='white',bg='blue', font=('Agency FB',12))
MoverAdelante.place(x=465,y=415)

LuzDImg = PhotoImage(file = 'BombilloD.png')
LucesDerecha = Button(root,image=LuzDImg,command=lambda:encenderluzderecha(None),fg='white',bg='blue', font=('Agency FB',12))
LucesDerecha.place(x=700,y=475)

LuzIImg = PhotoImage(file = 'Bombilloi.png')
LucesIzquierda = Button(root,image=LuzIImg,command=lambda:encenderluzizquierda(None),fg='white',bg='blue', font=('Agency FB',12))
LucesIzquierda.place(x=210,y=475)

EspecialBtn = Button(PatronFrame,text='Especial',command=lambda:especial(None),fg='white',bg='blue', font=('Agency FB',12),width=BtnWidth)
EspecialBtn.grid(row=4,pady=4)

ZigZagBtn = Button(PatronFrame,text='ZigZag',command=lambda:zigzag(None),fg='white',bg='blue', font=('Agency FB',12),width=BtnWidth)
ZigZagBtn.grid(row=3,pady=4)

CirculoDerechoBtn = Button(PatronFrame,text='Circulo Derecho',command=lambda:circuloderecho(None),fg='white',bg='blue', font=('Agency FB',12),width=BtnWidth)
CirculoDerechoBtn.grid(row=0,pady=4)

CirculoIzquierdoBtn = Button(PatronFrame,text='Circulo Izquierdo',command=lambda:circuloizquierdo(None),fg='white',bg='blue', font=('Agency FB',12),width=BtnWidth)
CirculoIzquierdoBtn.grid(row=1,pady=4)

LuzTImg = PhotoImage(file = 'LucesTra.png')
LucesDetras = Button(root,image=LuzTImg,command=lambda:encenderlucesdetras(None),fg='white',bg='blue', font=('Agency FB',12))
LucesDetras.place(x=536,y=560)

BtnInfinito = Button(PatronFrame,text='Infinito',command=lambda:infinito(None),fg='white',bg='blue', font=('Agency FB',12),width=BtnWidth)
BtnInfinito.grid(row=2,pady=4)

LuzFImg = PhotoImage(file = 'LucesFront.png')
LucesAdelante = Button(root,image=LuzFImg,command=lambda:encenderlucesadelante(None),fg='white',bg='blue', font=('Agency FB',12))
LucesAdelante.place(x=426,y=560)


#           _____________________________________
#__________/Creando el cliente para NodeMCU
myCar = NodeMCU()
myCar.start()

def get_log():
    
    Hilo que actualiza los Text cada vez que se agrega un nuevo mensaje al log de myCar
    

    global Result
    indice = 0
    # Variable del carro que mantiene el hilo de escribir.
    while(myCar.loop):
        while(indice < len(myCar.log)):
            valBool_fotocel = myCar.log[indice][1] #Valor booleano de la resistencia

            if int(valBool_fotocel) == 1:
                Result = "Nivel de luz apropiado"
            else:
                Result = "Nivel de luz bajo"
            
            FotoVal_result.config(text = Result)

            indice+=1
        time.sleep(0.200)
    
p = Thread(target=get_log)
p.start()
           

def moveradelante (event):
    myCar.send("1;")
    
def girarizquierda (event):
    myCar.send("3;")

def girarderecha (event):
    myCar.send("2;")

def encenderluzderecha (event):
    myCar.send("4;")

def encenderluzizquierda (event):
    myCar.send("5;")

def especial (event):
    myCar.send("12;")
    
def infinito (event):
    myCar.send("10;")

def zigzag (event):
    myCar.send("11;")

def circuloderecho (event):
    myCar.send("8;")

def circuloizquierdo (event):
    myCar.send("9;")

def encenderlucesdetras (event):
    myCar.send("7;")

def encenderlucesadelante (event):
    myCar.send("6;")

def Valor_foto (event):
    myCar.send("13;")

def sendShowID():
    
    Ejemplo como capturar un ID de un mensaje específico.
    
    mns = str(E_Command.get())
    if(len(mns)>0 and mns[-1] == ";"):
        E_Command.delete(0, 'end')
        mnsID = myCar.send(mns)
        messagebox.showinfo("Mensaje pendiente", "Intentando enviar mensaje, ID obtenido: {0}\n\
La respuesta definitiva se obtine en un máximo de {1}s".format(mnsID, myCar.timeoutLimit))
        
    else:
        messagebox.showwarning("Error del mensaje", "Mensaje sin caracter de finalización (';')")

def read():
    
    Ejemplo de como leer un mensaje enviado con un ID específico
    
    mnsID = str(E_read.get())
    if(len(mnsID)>0 and ":" in mnsID):
        mns = myCar.readById(mnsID)
        if(mns != ""):
            messagebox.showinfo("Resultado Obtenido", "El mensaje con ID:{0}, obtuvo de respuesta:\n{1}".format(mnsID, mns))
            E_read.delete(0, 'end')
        else:
            messagebox.showerror("Error de ID", "No se obtuvo respuesta\n\
El mensaje no ha sido procesado o el ID es invalido\n\
Asegurese que el ID: {0} sea correcto".format(mnsID))

    else:
        messagebox.showwarning("Error en formato", "Recuerde ingresar el separador (':')")


root.mainloop()
"""
