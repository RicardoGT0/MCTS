from random import uniform, seed
from time import time
import Nodo as Dyn_Nodo
from matplotlib.pyplot import scatter, savefig, figure, plot, clf
import pandas as pd
from os import mkdir

import comparativa
from calc_score import calc_score
from MCTS_UCT import MCTS_UCT
from funciones.Discus import Discus
from funciones.Bent import Bent
from funciones.HGBat import HGBat
from funciones.Ackley import Ackley
from funciones.Elliptic import Elliptic
from funciones.Expanded_GR import Expanded_GR
from funciones.Griewank import Griewank
from funciones.HappyCat import HappyCat
from funciones.Katsuura import Katsuura
from funciones.Rastrigin import Rastrigin
from funciones.Rosenbrock import Rosenbrock
from funciones.Scaffer import Scaffer
from funciones.Schwefels import Schwefels
from funciones.Weierstrass import Weierstrass
from funciones.Xcuadrada import Xcuadrada
from cec2013lsgo.cec2013 import Benchmark


def crear_inicio(tam_arreglo, rango):
    posicion = []
    seed()
    for n in range(tam_arreglo):
        posicion.append(uniform(rango[0], rango[1]))
    return posicion


def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

        # return string
    return str1

def graficar(num_nodos,y, funcion, ronda):
    x = range(1, num_nodos + 1)
    plot(x, y)
    n_funcion = str(funcion)[1:-1]
    n_fig = listToString([directorio + "/Figura_", n_funcion, "_", str(ronda), ".png"])
    savefig(n_fig, format="png")
    clf()

def run(rango=[-100, 100], num_dimension=10, num_nodos=100, num_ramas=5, presicion_sim=100, rondas=20, funcion=Xcuadrada, directorio=""):
    data = []
    Nodo = Dyn_Nodo.dyn_nodo(funcion)
    print(funcion)

    for ronda in range(rondas):
        t_inicial = time()

        inicio = crear_inicio(num_dimension, rango)
        MCTS = MCTS_UCT(Nodo, inicio, num_nodos, num_ramas, rango, presicion_sim, directorio)

        tiempo = time() - t_inicial
        valor_inicial = MCTS.nodo_inicial.getValor()
        vector_inicial = MCTS.nodo_inicial.getInformacion()
        mejor_valor = MCTS.Mejor_valor
        mejor_vector = MCTS.Mejor_vector
        data.append([funcion, ronda, vector_inicial, valor_inicial, mejor_valor, mejor_vector, tiempo])

        #graficar(num_nodos, MCTS.hist_valor, funcion, ronda)
    return data
    

if __name__ == "__main__":
    bench=Benchmark()
    try:
        mkdir("resultados")
    except:
        print("Error al crear el directorio /resultados")

    for nd in [100]:     #vector de prueba [50,300]
        for nr in [10]:    #vector de prueba [4,5,7,9]
            for p in [100]:      #vector de prueba [50,150,200,300]
                directorio = "resultados/resultados_N" + str(nd) + "_R" + str(nr) + "_P" + str(p)    
                try:
                    mkdir(directorio)
                    f = open('last_path.txt', 'w')
                    f.write(directorio)
                    f.close()
                except:
                    print("Error al crear el directorio ", directorio)

                data_funciones = []
                for f in range(1, 16):
                    info = bench.get_info(f)
                    dim = info['dimension']
                    low = info['lower']
                    upp = info['upper']
                    func_fit = bench.get_function(f)
                    func=type("func_" + str(f),(object,),{"func":func_fit})
                    data_funciones.extend(run(rango=[low,upp], num_dimension=dim, funcion=func,rondas=20, num_nodos= nd, num_ramas=nr, presicion_sim=p, directorio=directorio))

                dataframe = pd.DataFrame(data_funciones, columns=["Funcion", "Ronda", "Vector_Inicial", "Valor_Inicial", "Mejor_Valor", "Mejor_Vector", "Tiempo"])
                dataframe.to_csv(directorio + "/Resultados.csv")
    
                calc_score()
    comparativa.comparativa("resultados")
    data_comparativa = pd.DataFrame.from_dict(comparativa.dic_funciones, orient='index')
    data_comparativa.to_csv('resultados/comparativa.csv')
"""
    funciones = [Bent,
                 Discus,
                 Weierstrass,
                 Schwefels,
                 Katsuura,
                 HappyCat,
                 HGBat,
                 Expanded_GR,
                 Scaffer,
                 Rosenbrock,
                 Griewank,
                 Rastrigin,
                 Elliptic,
                 Ackley,
                 Xcuadrada]
    

"""
