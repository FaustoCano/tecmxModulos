# !/usr/bin/python
# -*- coding: utf-8 -*-
import os

class Carpeta():
    def __init__(self, var_direccion=".", var_crearCarpeta=True):
        """ var_dirección = es ls dirección de la carpeta a ser utilizada
         var_crearCarpeta = esta bandera es para indicar si se crea la carpeta, en caso de que no existir.

         Se  valida que la carpeta exista, en caso de no existir se crea la carpeta"""
        self.var_carpetaDireccion = var_direccion
        self.var_carpetaCrear = var_crearCarpeta

        self.met_carpetaExiste()
        self.met_carpetaCrear()

    def met_carpetaCrear(self):
        """Este metódo crea la carpeta.
        Valida la bandera de var_carpetaCrear y valida la var_carpetaExiste para crear la carpeta."""
        if self.var_carpetaCrear is True:
            if self.var_carpetaExiste is False:
                os.mkdir(self.var_carpetaDireccion)
            else:
                print("La carpeta ya existe")

    def met_carpetaExiste(self):
        """Este metódo valida si existe la caperta.
        var_carpetaExiste es verdadero si existe.
        var_carpetaExiste es falso si no existe."""

        var_consulta = os.path.exists(self.var_carpetaDireccion)

        if var_consulta == True:
            self.var_carpetaExiste = True
        else:
            self. existe = False

    def met_carpetaValidarSiEstaVacia(self):
        """Este metodo valida si la carpeta esta vacía.
        var_carpetaVacia es verdadero cuando esta vacia.
        var_carpetaVacia es falso cuando no esta vacia.
        """
        if self.var_carpetaExiste is True:
            var_listado = os.listdir(self.var_carpetaDireccion)
            if len(var_listado) == 0:
                self.var_carpetaVacia = True
            else:
                self.var_carpetaVacia = False

    def met_

    def met_carpetaMostrarExiste(self):
        """Este metódo muestra la variable var_carpetaExiste"""
        print(self.var_carpetaExiste)

    def met_carpetaMostrarCarpetaVacia(self):
        """Este metódo muestra la variable var_carpetaVacia"""
        print(self.var_carpetaVacia)


if __name__ == '__main__':
    objeto = Carpeta("./tmp")
    # help(objeto)
    objeto.met_carpetaMostrarExiste()
    objeto.met_carpetaValidarSiEstaVacia()



