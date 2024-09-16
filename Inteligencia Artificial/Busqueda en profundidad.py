# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 23:47:07 2024

@author: Angel Varela

Búsqueda en profundidad (DFS): Exploración de un laberinto
Situación cotidiana: Imagina que estás explorando un laberinto y quieres encontrar la salida. La búsqueda en profundidad implica explorar una ruta en profundidad antes de retroceder.

Algoritmo: Sigue una ruta hasta llegar a un callejón sin salida, luego retrocede y explora otra ruta.

"""

def busqueda_profundidad(laberinto, inicio, objetivo, visitados=None):
    if visitados is None:
        visitados = set()
    
    if inicio == objetivo:
        return f"Salida encontrada en {inicio}"
    
    visitados.add(inicio)
    
    for vecino in laberinto[inicio]:
        if vecino not in visitados:
            resultado = busqueda_profundidad(laberinto, vecino, objetivo, visitados)
            if resultado:
                return resultado
    return None

# Simulación de laberinto
laberinto = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'G'],
    'F': ['C'],
    'G': ['E']
}
resultado = busqueda_profundidad(laberinto, 'A', 'G')
print(resultado)
