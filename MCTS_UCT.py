from random import uniform
from math import sqrt, log


class MCTS_UCT():

    def __init__(self, nodo, inicio, num_nodos):
        self.Nodo = nodo
        self.nodo_inicial = self.Nodo(inicio)
        self.Mejor_vector = self.nodo_inicial.getInformacion()
        self.Mejor_valor = self.nodo_inicial.getValor()
        self.hist_valor = []
        self.__seguimiento=[]
        for i in range(num_nodos):
            self.__seguimiento = [self.nodo_inicial]
            nodo_actual = self.seleccion(self.nodo_inicial)
            nodo_actual.visitas += 1
            self.simulacion(nodo_actual)
            self.retropropagacion()
            self.hist_valor.append(nodo_actual.getValor())


    def nuevo_valor(self,origen):
        nuevo_vector = [0] * len(origen)
        for x in range(len(origen)):
            nuevo_vector[x] = uniform(origen[x] - 10, origen[x] + 10)
        return nuevo_vector


    def montecarlo_radial(self, origen):
        contador = 0
        presicion = 300
        # print (1/sqrt(presicion))

        for i in range(presicion):
            nodo_virtual = self.Nodo(self.nuevo_valor(origen))
            if (nodo_virtual.getValor() <= self.Mejor_valor):
                contador += 1

        porcentaje_exito = contador / presicion #cambio 100 * contador / presicion
        return porcentaje_exito


    def uct(self, nodo, nodo_Padre):
        Qs = nodo.ganacia
        Ns = nodo.visitas
        if Ns == 0:
            return 0
        Cp = 1
        s0 = nodo_Padre
        Ns0 = s0.visitas
        return (Qs / Ns) + (2 * Cp * sqrt(log(Ns0) / Ns))


    def mejorSucesorUCT(self, nodo_actual):
        uct_mejor = self.uct(nodo_actual.siguiente[0], nodo_actual)
        uct_nodo = nodo_actual.siguiente[0]
        for nodo in nodo_actual.siguiente:
            uct_actual = self.uct(nodo, nodo_actual)
            if uct_actual >= uct_mejor:  #cambio >=
                uct_nodo = nodo
        self.__seguimiento.append(uct_nodo)
        return uct_nodo


    def expande(self, nodo_actual):
        nuevo_nodo = 0
        if nodo_actual.siguiente: #No esta vacio
            nuevo_nodo = nodo_actual.siguiente[0]
        while (nuevo_nodo in nodo_actual.siguiente) or nuevo_nodo == 0:
            nuevo_nodo = self.Nodo(self.nuevo_valor(nodo_actual.getInformacion()))
        #evaluacion del nuevo nodo
        if (nuevo_nodo.getValor() < self.Mejor_valor):
            self.Mejor_valor = nuevo_nodo.getValor()
            self.Mejor_vector = nuevo_nodo.getInformacion()
        # Añadir un nuevo sucesor
        nodo_actual.siguiente.append(nuevo_nodo)
        self.__seguimiento.append(nuevo_nodo)
        return nuevo_nodo


    def seleccion(self, nodo_actual):
        if len(nodo_actual.siguiente) < 2:  # no está completamente expandido
            return self.expande(nodo_actual)
        else:
            while len(nodo_actual.siguiente) > 0:  # no sea terminal
                nodo_actual.visitas += 1
                nodo_actual = self.mejorSucesorUCT(nodo_actual)
            return self.expande(nodo_actual)


    def simulacion(self, nodo_actual):
        informacion = nodo_actual.getInformacion()
        nodo_actual.ganacia = self.montecarlo_radial(informacion)


    def retropropagacion(self):
        ganancia_general = self.__seguimiento[-1].ganacia
        for nodo in reversed(self.__seguimiento):
            if ganancia_general > nodo.ganacia:
                nodo.ganacia = ganancia_general


