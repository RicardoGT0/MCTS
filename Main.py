from random import uniform, seed
from time import time
import Nodo as Dyn_Nodo
from matplotlib.pyplot import scatter, savefig, figure, plot, clf
import pandas as pd
from os import mkdir

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

def run(rango = [-100, 100], num_dimension = 10, num_nodos = 100, num_ramas=5, presicion_sim=100):

    funciones=[Bent,
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

    data = []
    directorio= "resultados_D"+str(num_dimension)+"_N"+str(num_nodos)+"_R"+str(num_ramas)+"_P"+str(presicion_sim)
    try:
        mkdir(directorio)
        f = open('last_path.txt', 'w')
        f.write(directorio)
        f.close()
    except:
        print("El directorio ", directorio, " ya existe")
    for funcion in funciones:
        Nodo = Dyn_Nodo.dyn_nodo(funcion)
        print(funcion)

        for ronda in range(20):
            t_inicial = time()

            inicio = crear_inicio(num_dimension, rango)
            MCTS=MCTS_UCT(Nodo, inicio,num_nodos,num_ramas, rango, presicion_sim, directorio)

            tiempo = time() - t_inicial
            valor_inicial=MCTS.nodo_inicial.getValor()
            vector_inicial=MCTS.nodo_inicial.getInformacion()
            mejor_valor=MCTS.Mejor_valor
            mejor_vector=MCTS.Mejor_vector
            data.append([funcion, ronda, vector_inicial, valor_inicial, mejor_valor, mejor_vector, tiempo])


            x = range(1, num_nodos+1)
            plot(x,MCTS.hist_valor)
            n_funcion=str(funcion)[1:-1]
            n_fig = listToString([directorio+"/Figura_",n_funcion, "_", str(ronda),".png"])
            savefig(n_fig, format="png")
            clf()


    dataframe = pd.DataFrame(data, columns=["Funcion", "Ronda", "Vector_Inicial", "Valor_Inicial", "Mejor_Valor", "Mejor_Vector", "Tiempo"])
    dataframe.to_csv(directorio+"/Resultados.csv")

    calc_score()


if __name__ == "__main__":
    for nd in range(50,501,50):
        for nr in range(2,11):
            for p in range(50, 301, 50):
                run(num_nodos=nd,num_ramas=nr,presicion_sim=p)