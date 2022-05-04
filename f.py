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
    if len(lista) == 0:
        return [[nome, distancia]]
    elif len(lista) == 1:
        if distancia > lista[0][1]:
            lista.append([nome, distancia])
        else:
            lista.insert(0, [nome, distancia])
        return lista
    else:
        for i in range(len(lista)):
            if nome == lista[i][0]:
                return lista
            elif distancia < lista[i][1]:
                lista.insert(i, [nome, distancia])
                return lista
        lista.append([nome, distancia])
        return lista

#função que vereifica se esta dado pais esta na lista
def esta_na_lista(p, l):
    for i in l:
        if p in i:
            return True
    return False

#função que sorteia uma letra de uma palvra (desde que ela não esteja na lista restrita)
def sorteia_letra(p, lr):
    i = 0
    while True:
        if i == len(p) * 2:
            return ''
        s = random.choice(p.lower())
        if s not in lr and s.isalpha():
            break
    return s
    
#função que devolve a cor predominante da bandeira
def cor_bandeira(d):
    maior = 0
    for x, y in d.items():
        if y > maior:
            maior = y
            cor = x
    return cor

#função que remove letras duplicadas de uma palavra
def remove_duplicadas(str, n):
    s = set()

    for i in str:
        s.add(i)

    st = ""
    for i in s:
        st = st+i
    return st