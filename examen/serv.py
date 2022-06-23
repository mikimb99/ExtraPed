
import  socket, os, time, sys
import select


class Servidor:
    #TAL CUAL--------
    def abrir_socket(self):
        if not self.port:
            self.port= 16023 #poner el puerto que nos diga
        ruta="0.0.0.0"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((ruta, self.port))
        s.listen(1)
        self.lista_sockets.append(s)

        return s


    def mandar_msg(self,msg, socket):
        socket.send(msg.encode('utf8'))
    #-----------

    # ESTO IGUAL NO HACE FALTA
    # obtener_accion(linea)
    #opcion=l
    #campo=inea
    def obtener_accion(self,data):
        opcion=data[:1 ]
        campo= data[1:]
        return opcion,campo

    #ejemplo de funcion
    #HACER AQUI LAS FUNCIONES
    def sumar(self,a,b):
        return a+b

    def hora(self):
        return time.strftime("%H:%M:%S")

    def nlineas(self): #contar nº lineas de un archivo
        lines = 0
        size = 1024 * 1024
        with open('archivo.txt', "r+") as myfile:
            read_file = myfile.read
            buffer = read_file(size)
            while buffer:
                lines += buffer.count('\n')
                buffer = read_file(size)
        if (lines != 0):
            lines += 1
        print(lines)
    def espalindroma(self): #introduces por pantalla una palabra y mira si es palíndroma
        palabra = input("Introduce la palabra: ")
        # Imprime en ese caso "Es palindroma"
        if str(palabra) == str(palabra)[::-1]:
            print("Es palindroma: ", palabra)
        else:
            print("No es palindroma: ", palabra)
    def contarpalabras(self): #cuenta las palabras que hay en un archivo
        with open("archivo.txt") as f:
               contents = f.read()
               print(contents)
               palabras = contents.split() #split para convertirla en lista
               num_palabras= len(palabras)
               print("El archivo " + "archivo.txt" + " contiene: "+ str(num_palabras))
    #TAL CUAL-----
    def run_serv(self):
        self.socket = self.abrir_socket()
        while True:
            try:
                print("Esperando a que se conecte un cliente......")
                readyInput, _, _ = select.select(self.lista_sockets, [], [])

                for sock in readyInput:
                    if sock is self.socket:
                        conexion, direccion_cli = sock.accept()
                        print("conexión establecida con el cliente", direccion_cli)
                        print(direccion_cli) #imprimir direccion y puerto del cliente
                        self.lista_sockets.append(conexion)

                    else:
                        try:
                            print("espero un mensaje")
                            data = sock.recv(1024).decode("utf8")
                            #opcion, campo = self.obtener_accion(data)
                            if not data: #si se cierra el cliente que lo borre de la lista
                                self.lista_sockets.remove(sock)
                                break

                            mensaje=""
                            #------------------

                            #AQUI HACES LOS IFS PARA LAS FUNCIONES
                            if data== "hora":
                                mensaje = self.hora()
                            elif data == "fecha":
                                mensaje = time.strftime("%d/%m/%y")
                            elif data== "lineas":
                                mensaje = self.nlineas()
                            elif data== "palindroma":
                                mensaje = self.espalindroma()
                            elif data== "contar":
                                mensaje = self.contarpalabras()
                            else:
                                mensaje= "ERROR"
                            #if data=="sumar":
                            #mensaje= self.sumar(1,2)
                            #elif data== "restar":
                            #mensaje= self.rest

                            #MANDAR SOLUCION
                            if mensaje:
                               self.mandar_msg(mensaje,sock)
                            else:
                                  pass
                        #TAL CUAL, GESTION DE EXCEPECIONES
                        except OSError as exc:
                            if exc.errno == 54:
                                self.lista_sockets.remove(sock)
                            else:
                                raise exc
            #METODO PARA CERRAR EL SERVIDOR, QUE AVISA A TODOS LOS CLIENTES, TAL CUAL ¡NI ROZAR!
            except KeyboardInterrupt: #ctrl+c
                self.lista_sockets.remove(self.socket)
                if self.lista_sockets:
                    for n in self.lista_sockets:
                            self.mandar_msg("salir", n)

                self.socket.close()
                sys.exit(0)
            except:
                raise

    def __init__(self,port=None):
        self.port = port
        self.lista_sockets= []
        self.socket=None
        
if __name__ == "__main__":
    a= Servidor()
    a.run_serv()



