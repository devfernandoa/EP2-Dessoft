### ARQUIVO QUE CONTEM TODAS AS FUNÇÕES DO PROGRAMA	###

from math import *
import random

#função que normaliza um dicionario especifico
def normaliza(d):
    dr = {}
    for x, y in d.items():
        for a, b in y.items():
            dr[a] = b
            dr[a]['continente'] = x
    return dr
    