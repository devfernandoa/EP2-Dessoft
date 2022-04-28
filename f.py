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

#função que calcula a distância entre dois países usando a fórmula de Haversine
def haversine(r, p1, l1, p2, l2): 
    d = 2 * r * asin(sqrt(sin(radians((p2-p1)/2)) ** 2 + (cos(radians(p1)) * cos(radians(p2)) * (sin(radians((l2-l1)/2)) ** 2))))
    return d

#função que adiciona os países na lista com distâncias em ordem crescente
def adiciona_em_ordem(nome, distancia, lista):
    if lista == []:
        return [[nome, distancia]]
    elif len(lista) == 1:
        if distancia > lista[0][1]:
            lista.append([nome, distancia])
        else:
            lista.insert(0, [nome, distancia])
    else:
        for i in range(len(lista)):
            if (distancia > lista[i][1]) and (distancia < lista[i+1][1]):
                lista.insert(i+1, [nome, distancia])
    return lista