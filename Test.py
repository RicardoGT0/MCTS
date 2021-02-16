from random import uniform
from math import sqrt


def validacion_positiva(punto):
    return punto < 1


def montecarlo_radial(origen):
    contador=0
    presicion=1000000
    nuevo_vector = [0] * len(origen)
    for i in range(presicion):
        for x in range(len(origen)):
            nuevo_vector[x]=uniform(origen[x]-1,origen[x]+1)
        if validacion_positiva(nuevo_vector):
            contador+=1
    porcentaje_exito=100*contador/presicion
    print(porcentaje_exito)
    print (1/sqrt(presicion))

montecarlo_radial()