# !/usr/bin/python
# -*- coding: utf-8 -*-
import os

class Directorio():
    def __init__(self, var_par_direccion="./tmp", var_par_directorioCrear=True):
        """ var_dirección = es ls dirección de la directorio a ser utilizada
         var_par_directorioCrear = esta bandera es para indicar si se crea la directorio, en caso de que no existir.

         Se  valida que la directorio exista, en caso de no existir se crea la directorio"""
        self.var_directorioDireccion = var_par_direccion
        self.var_directorioCrear = var_par_directorioCrear

        self.met_directorioExiste()
        self.met_directorioCrear()
        self.met_directorioValidarSiEstaVacio()

    def met_directorioValidarSiEstaVacio(self):
        """Este metodo valida si la directorio esta vacía.
        var_directorioVacia es verdadero cuando esta vacia.
        var_directorioVacia es falso cuando no esta vacia.
        """
        if self.var_directorioExiste is True:
            var_listado = os.listdir(self.var_directorioDireccion)
            if len(var_listado) == 0:
                self.var_directorioVacia = True
            else:
                self.var_directorioVacia = False

    def met_directorioExiste(self):
        """Este metódo valida si existe la caperta.
        var_directorioExiste es verdadero si existe.
        var_directorioExiste es falso si no existe."""

        self.var_directorioExiste = os.path.exists(self.var_directorioDireccion)

    def met_directorioCrear(self):
        """Este metódo crea la directorio.
        Valida la bandera de var_directorioCrear y valida la var_directorioExiste para crear la directorio."""
        if self.var_directorioCrear is True:
            if self.var_directorioExiste is False:
                os.mkdir(self.var_directorioDireccion)
            else:
                print("El directorio ya existe")

    def met_directorioVaciar(self, var_eliminarArchivos=False):
        arr_archivosParaEliminar = os.listdir(self.var_directorioDireccion)
        var_tamArchivosParaEliminar = (len(arr_archivosParaEliminar))

        if var_tamArchivosParaEliminar != 0:
            print("Los siguientes archivos van a ser Eliminados:")
            for archivo in arr_archivosParaEliminar:
                print(archivo)

            if var_eliminarArchivos is True:
                for archivo in arr_archivosParaEliminar:
                    print(self.var_directorioDireccion + "/" + archivo)
                    os.remove(self.var_directorioDireccion + "/" + archivo)
                print("Se eliminaron los archivos.")
            else:
                print("La bandera para eliminar objetos no esta activa.")

    def met_directorioEliminar(self):
        """Este metódo vacia y elimina la carpeta señalada."""
        print("Vaciando Carpeta.")
        self.met_directorioVaciar(var_eliminarArchivos=True)
        print("Eliminado Carpeta.")
        try:
            os.rmdir(self.var_directorioDireccion)
        except:
            print("No se pudo eliminar la carpeta")

    def met_directorioMostrarExiste(self):
        """Este metódo muestra la variable var_directorioExiste"""
        print("Variable directorio = " + str(self.var_directorioExiste))

    def met_directorioMostrardirectorioVacio(self):
        """Este metódo muestra la variable var_directorioVacia"""
        print("Varialbe directorio Vacio = " + str(self.var_directorioVacia))


if __name__ == '__main__':
    objeto = Directorio("./tmp")
    # help(objeto)
    # objeto.met_directorioMostrarExiste()
    # objeto.met_directorioValidarSiEstaVacio()
    # objeto.met_directorioMostrardirectorioVacio()
    # objeto.met_directorioVaciar(var_eliminarArchivos=True)
    # objeto.met_directorioEliminar()



