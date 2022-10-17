#!/usr/bin/python3
# Created by Jesus257 at 08/10/22
# Software version 1.0.0

import os
class PersonalFile():
    def __init__(self,
                 var_directorio="./tmp",
                 var_nombreDelArchivo="prueba.txt",
                 var_banderaSobreEscribir=False,
                 var_directorioCrear=True):
        # inicializando variables
        self.var_directorio = var_directorio
        self.var_nombreArchivo = var_nombreDelArchivo
        self.var_SobreEscribir = var_banderaSobreEscribir
        self.rutaArchivo = self.var_directorio + "/" + self.var_nombreArchivo
        self.var_directorioCrear = var_directorioCrear

        # validando si existe el directorio.
        self.met_directorioExiste()

        # si la bandera de var_directorioCrear es verdadera se procede a crear el directorio
        if self.var_directorioCrear is True:
            # si la var_directorioExiste es Falso se crea el directorio.
            if self.var_directorioExiste is False:
                self.met_directorioCrear()
                self.met_directorioExiste()

    def met_directorioExiste(self):
        self.var_directorioExiste = os.path.exists(self.var_directorio)
    def met_directorioCrear(self):
        os.mkdir(self.var_directorio)
    def met_dierectorioMostarExiste(self):
        print(self.var_directorioExiste)
    def met_directorioVaciar(self, var_eliminarArchivos=False):
        arr_archivosParaEliminar = os.listdir(self.var_directorio)
        var_tamArchivosParaEliminar = (len(arr_archivosParaEliminar))

        if var_tamArchivosParaEliminar != 0:
            print("Los siguientes archivos van a ser Eliminados:")
            for archivo in arr_archivosParaEliminar:
                print(archivo)

            if var_eliminarArchivos is True:
                for archivo in arr_archivosParaEliminar:
                    os.remove(self.var_directorio + "/" + archivo)
    def met_directorioEliminar(self):
        self.met_directorioVaciar(var_eliminarArchivos=True)
        os.rmdir(self.var_directorio)

    def met_archivoCrear(self, arr_texto=["Hola mundo"]):
        f = open(self.rutaArchivo, "w")
        f.writelines(arr_texto)
        f.close()

    #def met_archivoAgregarTexto(self):

    def met_archivoLeer(self):
        f = open(self.rutaArchivo, 'r')
        mensaje = f.read()
        print(mensaje)
        f.close()

    def met_archivoVacio(self):
        self.met_archivoCrear("")

    def met_archivoEliminar(self):
        os.remove(self.rutaArchivo)

    def met_existe(self, var_direccion):
        var_existe = os.path.exists(var_direccion)
        if var_existe == True:
            print("existe")
        else:
            print("no existe")

    def met_existeCarpeta(self):
        self.met_existe(self.var_directorio)

if __name__ == '__main__':
    objeto = PersonalFile()
    objeto.met_archivoCrear(["buenas tardes", "como les va?"])
    objeto.met_archivoLeer()
    # objeto.met_directorioVaciar(var_eliminarArchivos=True)
    # objeto.met_directorioEliminar()
    #objeto.met_archivoVacio()
    #objeto.met_archivoLeer()
#    objeto.met_archivoEliminar()

