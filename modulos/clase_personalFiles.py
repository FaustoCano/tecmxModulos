#!/usr/bin/python3
# Created by Jesus257 at 08/10/22
# Software version 1.0.0

import os
class PersonalFile():
    def __init__(self, var_directorio=".", var_nombreDelArchivo="prueba.txt", var_banderaSobreEscribir=False):
        self.var_directorio = var_directorio
        self.var_nombreArchivo = var_nombreDelArchivo
        self.var_SobreEscribir = var_banderaSobreEscribir
        self.rutaArchivo = self.var_directorio + "/" + self.var_nombreArchivo

    def met_archivoCrear(self, texto="Hola mundo"):
        f = open(self.rutaArchivo, "w")
        f.write(texto)
        f.close()

    def met_archivoLeer(self):
        f = open(self.rutaArchivo, 'r')
        mensaje = f.read()
        print(mensaje)
        f.close()

    def met_archivoVacio(self):
        self.met_archivoCrear("")
    def met_archivoEliminar(self):
        os.remove(self.rutaArchivo)


if __name__ == '__main__':
    objeto = PersonalFile()
    objeto.met_archivoCrear("hola cuates como les va")
    objeto.met_archivoLeer()
    #objeto.met_archivoVacio()
    #objeto.met_archivoLeer()
#    objeto.met_archivoEliminar()