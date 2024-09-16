# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 23:48:50 2024

@author: Angel Varela

Búsqueda A*: Encontrando la ruta más rápida a un destino
Situación cotidiana: Estás conduciendo y quieres encontrar la ruta más rápida a tu destino usando un mapa. El algoritmo A* toma en cuenta tanto la distancia recorrida como la estimación de la distancia restante.

Algoritmo: Utiliza una combinación de la distancia desde el punto de partida y la distancia estimada al destino para explorar las rutas de manera eficiente.

"""

import heapq

def busqueda_a_estrella(grafo, inicio, objetivo):
    cola_prioridad = []
    heapq.heappush(cola_prioridad, (0, inicio))
    costos = {inicio: 0}

    while cola_prioridad:
        _, nodo_actual = heapq.heappop(cola_prioridad)

        if nodo_actual == objetivo:
            return f"Ruta más rápida a {objetivo} encontrada"

        for vecino, costo in grafo[nodo_actual].items():
            nuevo_costo = costos[nodo_actual] + costo
            if vecino not in costos or nuevo_costo < costos[vecino]:
                costos[vecino] = nuevo_costo
                prioridad = nuevo_costo
                heapq.heappush(cola_prioridad, (prioridad, vecino))
    return f"No se encontró ruta a {objetivo}"

# Simulación de mapa de rutas
mapa_rutas = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 2},
    'E': {'B': 5, 'G': 1},
    'F': {'C': 3},
    'G': {'E': 1}
}
resultado = busqueda_a_estrella(mapa_rutas, 'A', 'G')
print(resultado)
