# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 23:45:30 2024

@author: Angel Varela

Búsqueda en anchura (BFS): Explorando conexiones en una red social
Situación cotidiana: Quieres encontrar la conexión más corta entre dos personas en una red social (amigos de amigos). Utilizarás la búsqueda en anchura para explorar todas las conexiones en un nivel antes de pasar al siguiente.

Algoritmo: Explora todas las personas a las que el primer usuario está conectado, luego las conexiones de esas personas, y así sucesivamente, hasta encontrar al amigo objetivo.

"""

from collections import deque

def busqueda_anchura(red_social, inicio, objetivo):
    cola = deque([inicio])
    visitados = set()

    while cola:
        persona = cola.popleft()
        if persona == objetivo:
            return f"{objetivo} encontrado"
        visitados.add(persona)
        for amigo in red_social[persona]:
            if amigo not in visitados:
                cola.append(amigo)
    return f"{objetivo} no está conectado a {inicio}"

# Simulación de red social
red_social = {
    'Ana': ['Carlos', 'David'],
    'Carlos': ['Ana', 'Juan'],
    'David': ['Ana', 'Sara'],
    'Juan': ['Carlos'],
    'Sara': ['David']
}
resultado = busqueda_anchura(red_social, 'Ana', 'Juan')
print(resultado)
