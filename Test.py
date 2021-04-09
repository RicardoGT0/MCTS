from random import uniform
from math import sqrt
import pandas as pd
from cec2013lsgo.cec2013 import Benchmark
from numpy.random import rand
from os import mkdir

directorio1 = "resultados"
directorio2 = "resultados/resultados_D"
try:
    mkdir(directorio1)
    mkdir(directorio2)
    f = open('last_path.txt', 'w')
    f.write(directorio2)
    f.close()

except:
    print("El directorio ", directorio2, " ya existe")

"""
def dyn_nodo(tipo):
    class Nodo (tipo):
        def __init__(self, sol):
            resultado = self.fun_fitness(sol)
            print(resultado)
    return Nodo

bench = Benchmark()
for f in range(1,16):
    info = bench.get_info(f)
    dim = info['dimension']
    sol = info['lower']+rand(dim)*(info['upper']-info['lower'])
    fun_fitness = bench.get_function(f)

    print(info)


def validacion_positiva(punto):
    return punto < 1


def montecarlo_radial(origen):
    contador = 0
    presicion = 1000000
    nuevo_vector = [0] * len(origen)
    for i in range(presicion):
        for x in range(len(origen)):
            nuevo_vector[x] = uniform(origen[x] - 1, origen[x] + 1)
        if validacion_positiva(nuevo_vector):
            contador += 1
    porcentaje_exito = 100 * contador / presicion
    print(porcentaje_exito)
    print(1 / sqrt(presicion))


# montecarlo_radial()


data = {
    '1': {
        'apple': 11,
        'banana': 18},
    '2': {
        'apple': 16,
        'banana': 12}
}
print(data)

a = {k: pd.Series(v) for k, v in data.items()}

a = {}
for k, v in data.items():
    for x, z in v.items():
        a[k] = pd.Series(z)

print(a)
"""