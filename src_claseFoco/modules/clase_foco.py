#!/usr/bin/python3
# Created by Jesus257 at 01/10/22
# Software version 1.0.0

class Foco:
    def __init__(self,nombreExterior):
        self.nombre = nombreExterior
        self.met_mostrarNombre()
        self.met_apagarfoco()

# ---------------------------------------------------------
    def met_mostrar(self,nombre):
        print("el nombre del objeto es: " + nombre)

    def met_mostrarNombre(self):
        print("el nombre del objeto es: " + self.nombre)

    def met_actualizarNombre(self):
        self.nombre = input("Escribe el nombre:")

# ---------------------------------------------------------
    def met_estadodefoco(self):
        print("El estado del foco es " + str(self.estadodefoco))

    def met_encenderfoco(self):
        print("----- Encenciendo el Foco -----")
        self.estadodefoco = True
        self.met_estadodefoco()

    def met_apagarfoco(self):
        print("----- Apagar el Foco -----")
        self.estadodefoco = False
        self.met_estadodefoco()

if __name__ == '__main__':

    jorge = Foco("jorge")
    #angel = Foco("angel")
    #imelda= Foco("Imelda")
    jorge.met_mostrarNombre()
    #angel.met_mostrarNombre()
    #imelda.met_mostrarNombre()
    #imelda.met_mostrar("prueba")
    jorge.met_estadodefoco()
    jorge.met_encenderfoco()
    jorge.met_estadodefoco()
    jorge.met_apagarfoco()
    jorge.met_estadodefoco()
