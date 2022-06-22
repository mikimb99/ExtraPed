import socket, time,sys, select

class Cliente:
    #
    def mandar_msg(self,msg,socket):
        socket.send(msg.encode('utf8'))

    def tratamiento_respuesta(self, respuesta):
        if respuesta=="salir":
            print("Servidor desconectado :(")
            sys.exit(0)


        else:
            print(respuesta)





    def cli7(self):
       #TAL CUAL----
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        #puerto = int(input("Introduce el puerto del servidor: "))
        puerto= 16023
        s.connect(("localhost", puerto))

        lista_sockets = [s, sys.stdin]

        try:
            while True: #si dice 3 mensajes solo, cambiar whhile tru por el for
                #-------
                #si quieres hacer un print, es aqui
                #print ("Dime linea o frase")
                #TALCUAL
                readyInput, _, _ = select.select(lista_sockets, [], [])

                for fd in readyInput:
                    if fd == sys.stdin:
                        teclado= input()

                        if teclado:
                            self.mandar_msg(teclado,s)
                            if teclado=="salir":
                                print("Adios")
                                sys.exit(0)

                    else:
                        res= s.recv(1024).decode("utf8")
                        if res:
                            self.tratamiento_respuesta(res)




        except OSError as exc:
            if exc.errno == 61 or exc.errno == 54:  # 32 es broken pipe
                print("WARNING: Servidor desconectado :( ")
            else:
                raise exc





if __name__ == "__main__":
    client = Cliente()
    client.cli7()