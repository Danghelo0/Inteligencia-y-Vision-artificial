# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 22:36:45 2024

@author: PC
"""

import pandas as pd

V = list('abcdefgh')
grafoa = pd.DataFrame(index=V, columns=V)
grafoa.loc['a', ['b', 'c', 'g']] = 1
grafoa.loc['b', ['a', 'd', 'g']] = 1
grafoa.loc['c', ['a', 'd', 'e']] = 1
grafoa.loc['d', ['b', 'c', 'f']] = 1
grafoa.loc['e', ['c', 'f', 'g']] = 1
grafoa.loc['f', ['d', 'e', 'h']] = 1
grafoa.loc['g', ['a', 'b', 'e']] = 1
grafoa.loc['h', ['f']] = 1
# grafoa = grafoa.fillna(0)  # Llenar los valores NaN con 0
# grafoa.to_json("grafoa.json",orient='split')

def Prof(grafoa, nodo_inicial):
    visitados = set()
    arbol_expansion = []

    def explorar(nodo, visitados, arbol_expansion):
        visitados.add(nodo)
        for vecino in grafoa.columns[(grafoa.loc[nodo] > 0)]:
            if vecino not in visitados:
                arbol_expansion.append((nodo, vecino))
                explorar(vecino, visitados, arbol_expansion)

    explorar(nodo_inicial, visitados, arbol_expansion)
    return arbol_expansion

arbol_expansion = Prof(grafoa, 'a') # nodo principal, cambiar para que cumpla el algoritmo en cualquier nodo
print("Árbol de expansión por profundidad:", arbol_expansion)
