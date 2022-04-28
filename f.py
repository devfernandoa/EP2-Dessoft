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
    
#função que sorte um país entre a lista de países
def sorteia_pais(nomes_de_paises):
    paises = []
    for i in nomes_de_paises:
        paises.append(i)
    pais = random.choice(paises)
    return pais

#calcula a distância entre dois países usando a fórmula de Haversine
def haversine(r, p1, l1, p2, l2): 
    d = 2 * r * asin(sqrt(sin(radians((p2-p1)/2)) ** 2 + (cos(radians(p1)) * cos(radians(p2)) * (sin(radians((l2-l1)/2)) ** 2))))
    return d