"""
Instituto TecnolÃ³gico de Costa Rica
Computer Engineering
Taller de ProgramaciÃ³n

Cliente python Formula E CE Tec
Proyecto 2, semestre 1
2019

Profesor: Milton Villegas Lemus
Autor: Santiago Gamboa RamÃ­rez

Restricciónes: Python3.7

Código para realizar la conexión con el servidor del NodeMCU
"""

#           ___________________________           
#__________/Bibliotecas utilizadas
from threading import Thread
import threading
import socket
import time

#           ___________________________           
#__________/Clase NodeMCU
class NodeMCU(Thread):
    """
    Clase que simplifica el funcionamiento del socket para el servidor en el NodeMCU
    Hereda de la clase Thread, para escribir siempre que tenga mensajes pendientes.
    Se hace con un Thread para no detener la ejecución del programa.
    Su ejecución es independiente. Por lo tanto hay un tiempo en el que se envía el mensaje y se lee la respuesta
    que debe tomarse en consideración, varibles como busy o el len(log) permiten conocer si se recibió un nuevo mensaje. 
    """
    #           ___________________________           
    #__________/Variables de la clase
    node_address = ()           #Dirección del servidor ip, puerto
    log = []                    #Lista de todos los mensajes enviados, con el resultado [[mensaje,respuesta],[mensaje,respuesta]]
    pending_mns = []            #Mensajes pendientes por enviar
    received_mns = []           #Mensajes recibidos pendientes por leer
    error_list = []             #Mensajes de error que generó python
    busy = False                #Variable para saber si se está enviando un mensaje
    error = False               #Variable para saber si el último mensaje fue erroneo
    interval = 0.100            #Intervalo para escribir nuevos mensajes
    loop = False                #Variable que controla el loop infinito
    timeoutLimit = 3       #Tiempo de espera por la respuesta.
    
    
    #           ___________________________           
    #__________/Constructor de la clase
    def __init__(self, ip = '192.168.43.200', port = 7070):
        Thread.__init__(self)
        self.node_address = (ip,port)
        
    #           _____________________________________   
    #__________/Función del Thread que se reescribe
    def run(self):
        """
        Esta funciónn se llama al ejecutar NodeMCU.start()
        Función heredada de la clase Thread, crea un hilo que escribe los mensajes pendientes en el socket cada intervalo de tiempo.
        Si hay más de un mensaje pendiente en la lista, los concatena para crear uno solo mensaje que puede manejar el servidor.
        Todo mensaje enviado recibe una respuesta.
        Entradas
            self : Guarda la referencia del objeto que se esta utilizando.
            self.loop : Variable que permite detener el hilo.
        Salidas
            Envia los mensajes pendientes al servidor.
       
        """
        self.loop = True
        while(self.loop):
            if(len(self.pending_mns)>0):
                self.busy = True
                message = ""
                #Contatenación de los mensajes pendientes
                for i in self.pending_mns:
                    message+=i
                    self.pending_mns.remove(i)
                message+="\r"
                
                #Variable local
                new_log = [message,""]
                
                #Intenta conectarse al servidor con la IP y Puertos definidos.
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    #Define el tiempo límite de espera
                    sock.settimeout(self.timeoutLimit)
                    sock.connect(self.node_address)
                    
                    #Intenta enviar los mensajes y espera por la respuesta.
                    try:
                        sock.sendall(message.encode())
                        data=b''
                        response = ""
                        while data != b'\r':
                            data = sock.recv(1)
                            response+=data.decode("utf-8")

                        self.received_mns.append(response)
                        new_log[1] = response

                        #Si hubo un error y el se envía correctamente se niega la variable error. 
                        if(self.error) :
                            self.error = False

                    #Se crea el socket y se conecta exitosamente pero no tiene respuesta.
                    #Errores de timeout
                    except socket.timeout as error:
                        print("Sin respuesta del servidor\nSe espera por", self.timeoutLimit,"s")
                        self.error=True
                        self.error_list.append(error)
                        new_log[1] = str(error)
                    #Error de tipo distinto a timeout  
                    except Exception as a:
                        print("Error al enviar al servidor\n\
                        Se espera por", self.timeoutLimit,"s")
                        print(str(a))
                        self.error=True
                        self.error_list.append(a)
                        new_log[1] = str(a)
                    #Solo se desconecta el socket si se conectó anteriormente.                          
                    finally:
                        sock.close()
                        
                #No se pudo conectar con el servidor          
                except Exception as e:
                    print("No se pudo conectar con el servirdor\n\
                    Verifique que ambos dispositivos están conectados y en la misma red")
                    print(str(e))
                    self.error=True
                    self.error_list.append(e)
                    new_log[1] = str(e)

                #Se agrega el resultado y el mensaje al log
                #Se desocupa el socket
                self.log.append(new_log)            
                self.busy = False
                
            time.sleep(self.interval)

    #           _____________________________________________
    #__________/Detiene el ciclo infinito de la función run
    def stop(self):
        self.loop = False
        
    #           ______________________________________ 
    #__________/Función para enviar mensajes al carro
    def send(self,message):
        """
        Agrega el mensaje de entrada a la lista de mensajes pendientes.
        Permite ser llamada desde cualquier parte del código
        Entradas
            self: Guarda la referencia al objeto que se esta utilizando.
            message: El mensaje que se desea enviar al servidor
        Salidas
            mnsID: Retorna un ID del mensaje enviado para que se pueda leer despues.
        Restricciones
            * El mensaje debe terminar con ; para que sea valido.
            * Si se desea utilizar el ID del mensaje, no debe ir acompañado de otro comando.
        """
        mnsID = ""
        if(self.loop):
            if(isinstance(message,str) and len(message)>0 and message[-1]==";"):
                self.pending_mns.append(message)
                mnsID = "{0}:{1}".format(str(len(self.log)), str(len(self.pending_mns)-1))
        else:
            print("Start the loop before trying to send messages")

        return mnsID
    #           ______________________________________ 
    #__________/Función para leer un mensaje del carro
    def read(self):
        """
        Retorna el último mensaje recibido del cliente y lo elimina de la lista de recibidos.
        Entradas 
            self: Guarda la referencia al objeto que se esta utilizando.
        Salida
            response: Ultimo mensaje respondido desde el servidor y que no fue leido previamente.
            retorna '' si no hay mensajes en la lista de mensajes recibidos por leer.
        Restricciones
        """
        response = ""
        if(len(self.received_mns)>0):
            response = self.received_mns.pop()
        return response

    #           _______________________________________________
    #__________/Función para leer un mensaje específico del log
    def readById(self, id):
        """
        Retorna el elemento del registro donde se incluye el mensaje y la respuesta del cliente.
        No elimina el mensaje de la lista de recibidos.
        Entradas
            self:   Guarda la referencia al objeto que se esta utilizando.
            id:     Identificador del mensaje. Se genera en la funcion send,
                    Esta compuesto por 2 indices, separados por ':' ejm = a:b
                        a = indice del log.
                        b = indice de pendientes antes de ser enviado.
        Salidas
            response:   
        """
        response = ""
        if(isinstance(id,str) and ":" in id):
           index = id.split(":")
           i = index[0]
           subi =index[1]
           if(i.isdigit() and subi.isdigit()):
               i = int(i)
               subi = int(subi)
               if(i<len(self.log)):
                   response = self.log[i][1].split(";")[subi]
               else:
                   print("No se ha enviado el mensaje")
        return response
        
               
    #           ______________________________________ 
    #__________/Función para leer todos los mensajes   
    def readAll(self):
        """
        Retorna una copia de la lista con todos los mensajes no leídos
        Vacía la lista de mensajes 
        Entradas
            self: Guarda la referencia al objeto que se esta utilizando.
        Salidas
            temp: Copia de la lista de mensajes recibidos.
        """
        temp = self.received_mns.copy()
        self.received_mns = []
        return temp

    #           ______________________________________ 
    #__________/Función para leer mensajes del carro
    def readLog(self):
        """
        Retorna una copia del log de mensajes, con todos los mensajes enviados y recibidos hasta el momento.
        Entradas
            self: Guarda la referencia al objeto que se esta utilizando.
        Salidas
            temp_log: Copia del log de mensajes. 
        """
        temp_log = self.log.copy()
        return temp_log
    
    #           ____________________________________________________________
    #__________/Función para leer errores en python que no llegaron al Carro
    def readError(self):
        """
        Retorna el último error generado desde python
        Entradas
            self: Guarda la referencia al objeto que se esta utilizando.
        Salidas
            error: Retorna el ultimo error que ocurrio
        """
        error = ""
        if(len(self.error_list)>0):
            error = self.error_list.pop()
        return error
        
