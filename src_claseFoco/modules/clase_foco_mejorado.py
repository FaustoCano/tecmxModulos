#!/usr/bin/python3
# Created by Jesus257 at 01/10/22
# Software version 1.0.0
from clase_foco import Foco

class FocoLed(Foco):

    def __init__(self, nombreExterior, var_tipo="led", var_lumen="100"):
        Foco.__init__(self,nombreExterior)
        self.tipo = var_tipo
        self.lumenes = var_lumen

    def met_mostrarTipo(self):
        print("Mostrar tipo: " + self.tipo)

    def met_agregarLumenes(self):
        self.lumenes = str(input("escribe un numero\n"))

    def met_mostrarLumenes(self):
        print("Los lumenes del foco son: " + self.lumenes )

if __name__ == '__main__':

    jorge = FocoLed(var_tipo="incandencente", nombreExterior="jorge", var_lumen="1000")
    jorge.met_mostrarTipo()
    jorge.met_mostrarLumenes()
  #  jorge.met_mostrarNombre()
  #  jorge.met_estadodefoco()
  #  jorge.met_encenderfoco()
  #  jorge.met_estadodefoco()
  #  jorge.met_apagarfoco()
  #  jorge.met_estadodefoco()
  #  jorge.met_mostrarTipo()
  #  jorge.met_agregarLumenes()
  #  jorge.met_mostrarLumenes()