# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 23:58:26 2024

@author: Angel Varela

Búsqueda con Ternary Search (Búsqueda ternaria): Encontrar la temperatura ideal en un día
Situación cotidiana: Imagina que estás buscando la temperatura más cómoda durante el transcurso de un día. Tienes acceso a los datos de temperatura por hora y deseas encontrar el mejor momento para salir, en función de la temperatura.

Algoritmo: La búsqueda ternaria es una mejora de la búsqueda binaria para encontrar el mínimo o máximo en una función unimodal (una función que tiene solo un punto máximo o mínimo). Divide el intervalo en tres partes y decide cuál parte explorar según la tendencia de la función.

"""

def busqueda_ternaria(temperaturas, izquierda, derecha):
    while derecha - izquierda > 1:
        tercio_izq = izquierda + (derecha - izquierda) // 3
        tercio_der = derecha - (derecha - izquierda) // 3

        if temperaturas[tercio_izq] < temperaturas[tercio_der]:
            derecha = tercio_der
        else:
            izquierda = tercio_izq
    return (izquierda + derecha) // 2

# Simulación de temperaturas durante el día (en horas)
temperaturas_dia = [25, 24, 23, 22, 21, 20, 21, 22, 23, 24, 25]  # Temperatura a lo largo de las horas
mejor_hora = busqueda_ternaria(temperaturas_dia, 0, len(temperaturas_dia) - 1)
print(f"La mejor hora para salir es a las {mejor_hora} horas con una temperatura de {temperaturas_dia[mejor_hora]}°C")
