# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 00:03:53 2024

@author: Angel Varela

Imagina que tienes un grafo donde los nodos son ciudades, y las aristas (conexiones) tienen tres atributos: distancia, peaje y tráfico. Tu objetivo es encontrar la ruta más barata, donde el costo total es una combinación ponderada de distancia, costo de peaje y tiempo adicional debido al tráfico.

El algoritmo utilizará la heurística de la distancia directa (como el vuelo de un pájaro) para aproximar la distancia al destino, pero considerará los otros factores a la hora de calcular el costo total.

"""

import heapq

# A* Algorithm with Multiple Costs: distance, toll, traffic
def a_star_multiple_costs(grafo, heuristica, inicio, objetivo):
    # Cola de prioridad para los nodos abiertos (costo total, nodo actual)
    cola_prioridad = []
    heapq.heappush(cola_prioridad, (0, inicio))
    
    # Diccionario para almacenar el costo mínimo para llegar a cada nodo
    costos = {inicio: 0}
    
    # Diccionario para rastrear los caminos recorridos
    camino = {inicio: None}
    
    while cola_prioridad:
        costo_actual, nodo_actual = heapq.heappop(cola_prioridad)
        
        # Si llegamos al objetivo, reconstruimos el camino
        if nodo_actual == objetivo:
            ruta_final = []
            while nodo_actual:
                ruta_final.append(nodo_actual)
                nodo_actual = camino[nodo_actual]
            ruta_final.reverse()
            return ruta_final, costos[objetivo]
        
        # Recorremos los vecinos del nodo actual
        for vecino, atributos in grafo[nodo_actual].items():
            # Costo total para el vecino: suma ponderada de distancia, peaje y tráfico
            distancia = atributos['distancia']
            peaje = atributos['peaje']
            trafico = atributos['trafico']
            
            # Fórmula del costo total: distancia + peaje + un peso para el tráfico
            costo_nuevo = costos[nodo_actual] + distancia + peaje + trafico * 0.5
            
            # Si encontramos un camino más barato hacia el vecino, lo añadimos
            if vecino not in costos or costo_nuevo < costos[vecino]:
                costos[vecino] = costo_nuevo
                prioridad = costo_nuevo + heuristica[vecino][objetivo]
                heapq.heappush(cola_prioridad, (prioridad, vecino))
                camino[vecino] = nodo_actual
    
    # Si no se encontró ninguna ruta, devolvemos un error
    return None, float('inf')

# Heurística (distancia directa "en línea recta") entre las ciudades
heuristica = {
    'A': {'B': 10, 'C': 15, 'D': 20, 'E': 25},
    'B': {'A': 10, 'C': 7, 'D': 25, 'E': 20},
    'C': {'A': 15, 'B': 7, 'D': 10, 'E': 30},
    'D': {'A': 20, 'B': 25, 'C': 10, 'E': 5},
    'E': {'A': 25, 'B': 20, 'C': 30, 'D': 5}
}

# Grafo con ciudades y atributos de las rutas (distancia, peaje y tráfico)
grafo = {
    'A': {
        'B': {'distancia': 10, 'peaje': 5, 'trafico': 3},
        'C': {'distancia': 15, 'peaje': 10, 'trafico': 1}
    },
    'B': {
        'A': {'distancia': 10, 'peaje': 5, 'trafico': 3},
        'C': {'distancia': 7, 'peaje': 2, 'trafico': 5},
        'D': {'distancia': 25, 'peaje': 8, 'trafico': 2}
    },
    'C': {
        'A': {'distancia': 15, 'peaje': 10, 'trafico': 1},
        'B': {'distancia': 7, 'peaje': 2, 'trafico': 5},
        'D': {'distancia': 10, 'peaje': 3, 'trafico': 1}
    },
    'D': {
        'B': {'distancia': 25, 'peaje': 8, 'trafico': 2},
        'C': {'distancia': 10, 'peaje': 3, 'trafico': 1},
        'E': {'distancia': 5, 'peaje': 1, 'trafico': 0}
    },
    'E': {
        'D': {'distancia': 5, 'peaje': 1, 'trafico': 0}
    }
}

# Encontrar la ruta más óptima de A a E
ruta, costo_total = a_star_multiple_costs(grafo, heuristica, 'A', 'E')
print(f"Ruta más óptima: {ruta}")
print(f"Costo total de la ruta: {costo_total}")
