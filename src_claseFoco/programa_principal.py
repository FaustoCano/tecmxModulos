#!/usr/bin/python3
# Created by Jesus257 at 01/10/22
# Software version 1.0.0
# -*- coding: utf-8 -*-

import os
import logging

from modules.clase_foco import Foco
from modules.clase_foco_mejorado import FocoLed

#__________________________________________________________
var_salida = False

os.system("clear")
print("Menú de la clase FOCO")
var_nombre = input("Ingresa un nombre:\n")
objeto = FocoLed(var_nombre)

while var_salida is not True:
    os.system("clear")
    print("\n\n¿Que deseas hacer?")
    print("1) Prender Foco")
    print("2) Apagar Foco")
    print("3) Cambiar nombre")
    print("4) Mostrar nombre")
    print("5) Mostrar estado")

    var_entrada = input("\n")

    if var_entrada == "1":
        objeto.met_encenderfoco()
    elif var_entrada == "2":
        objeto.met_apagarfoco()
    elif var_entrada == "3":
        objeto.met_actualizarNombre()
    elif var_entrada == "4":
        objeto.met_mostrarNombre()
    elif var_entrada == "5":
        objeto.met_estadodefoco()
    else:
        print("Este valor no esta permidido")

    print('''¿Desea salir?
    1) Sí
    2) No''')
    var_salidaMenu = input("\n")

    if var_salidaMenu == "1":
        var_salida = True

print("Gracias por usar el servicio.")