# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 23:43:46 2024

@author: Angel Varela


Búsqueda binaria: Buscando el nombre de una persona en una lista ordenada
Situación cotidiana: Tienes una lista de nombres de personas en orden alfabético y necesitas encontrar si un amigo está en la lista. Utilizarás la búsqueda binaria para reducir el número de comparaciones.

Algoritmo: Comienza buscando el nombre en la mitad de la lista. Si el nombre está antes de la mitad, busca en la primera mitad; si está después, busca en la segunda mitad.

"""

def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return f"{objetivo} encontrado en la posición {medio}"
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return f"{objetivo} no está en la lista"

# Simulación de lista de nombres ordenada
nombres = ['Ana', 'Carlos', 'David', 'Juan', 'Pedro', 'Sara']
resultado = busqueda_binaria(nombres, 'Juan')
print(resultado)
