# -*- coding: utf-8 -*-
from funciones.Discus import Discus

def dyn_nodo(tipo):
    class Nodo (tipo):
        def __init__(self, informacion):
            #print(tipo)
            self.__informacion = informacion
            self.siguiente = []
            self.visitas = 0
            self.ganacia = 0
            self.__valor = self.func(informacion)

        def getInformacion(self):
            return self.__informacion

        def getValor(self):
            return self.__valor

    return Nodo
