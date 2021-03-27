from random import uniform
from math import sqrt, log
from matplotlib.pyplot import scatter, savefig, figure, plot, clf, close, gca


class MCTS_UCT():

    def __init__(self, nodo, inicio, num_nodos, num_ramas, rango_op, presicion_simulacion, directorio=""):
        self.Nodo = nodo
        self.nodo_inicial = self.Nodo(inicio)
        self.Mejor_vector = self.nodo_inicial.getInformacion()
        self.Mejor_valor = self.nodo_inicial.getValor()
        self.hist_valor = []
        self.__directorio = directorio + "/"
        self.__seguimiento=[]
        self.__presicion_simulacion=presicion_simulacion
        self.__num_ramas=num_ramas
        self.__rango_min = rango_op[0]
        self.__rango_max = rango_op[1]

        for i in range(num_nodos):
            self.__seguimiento = [self.nodo_inicial]
            nodo_actual = self.seleccion(self.nodo_inicial)
            nodo_actual.visitas += 1
            self.simulacion(nodo_actual)
            self.retropropagacion()
            self.hist_valor.append(nodo_actual.getValor())
            if len(inicio)<=3:
                self.grafica(i)
        clf()

    def grafica(self,i):
        cont=0
        tipo=""
        lx=[]
        ly=[]
        lz=[]
        dimension=len(self.nodo_inicial.getInformacion())
        for nodo in self.__seguimiento:
            tipo=str(nodo.get_tipo())[1:-1]
            if len(nodo.getInformacion())==2:
                x,y=nodo.getInformacion()
                z=nodo.getValor()
                cont+=1
                lx.append(x)
                ly.append(y)
                lz.append(z)
        if dimension==3:
            #codigo para grafica 3D
            gca(projection='3d')
            plot(lx, ly, lz, label=tipo+str(i))
        else:
            plot(lx, ly)
        n_fig=(self.__directorio+"traza", tipo, str(i), ".png")
        savefig("_".join(n_fig), format="png")

    def nuevo_valor(self,origen):
        nuevo_vector = [self.__rango_max+1] * len(origen)
        for x in range(len(origen)):
            while nuevo_vector[x] < self.__rango_min or nuevo_vector[x] > self.__rango_max:
                nuevo_vector[x] = uniform(origen[x] - 5, origen[x] + 5)
        return nuevo_vector


    def montecarlo_radial(self, origen):
        contador = 0
        presicion = self.__presicion_simulacion
        # print (1/sqrt(presicion))

        for i in range(presicion):
            nodo_virtual = self.Nodo(self.nuevo_valor(origen))
            if (nodo_virtual.getValor() <= self.Mejor_valor):
                contador += 1
            if len(nodo_virtual.getInformacion()) == 2:
                x=nodo_virtual.getInformacion()[0]
                y=nodo_virtual.getInformacion()[1]
                scatter(x,y, color='black',alpha=0.3)

        porcentaje_exito = contador / presicion #cambio 100 * contador / presicion
        return porcentaje_exito


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


    def mejor_opcion(self, nodo_actual):
        mejor_opcion=0
        resultado=0
        for nodo in nodo_actual.siguiente:
            if resultado <= nodo.ganacia:
                mejor_opcion=nodo
                resultado=nodo.ganacia
        self.__seguimiento.append(mejor_opcion)
        return mejor_opcion


    def seleccion(self, nodo_actual):
        while len(nodo_actual.siguiente) >= self.__num_ramas:
            nodo_actual.visitas += 1
            nodo_actual = self.mejor_opcion(nodo_actual)
        return self.expande(nodo_actual)


    def simulacion(self, nodo_actual):
        informacion = nodo_actual.getInformacion()
        nodo_actual.ganacia = self.montecarlo_radial(informacion)


    def retropropagacion(self):
        ganancia_general = self.__seguimiento[-1].ganacia
        for nodo in reversed(self.__seguimiento):
            if ganancia_general > nodo.ganacia:
                nodo.ganacia = ganancia_general


