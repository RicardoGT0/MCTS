# -*- coding: utf-8 -*-
import numpy as np
def dyn_nodo(tipo):
    class Nodo (tipo):
        def __init__(self, informacion):
            self.__informacion = informacion
            self.siguiente = []
            self.visitas = 0
            self.ganacia = 0
            self.__valor = self.func(np.array(informacion))

        def getInformacion(self):
            return self.__informacion

        def getValor(self):
            return self.__valor

        def get_tipo(self):
            return tipo

    return Nodo
