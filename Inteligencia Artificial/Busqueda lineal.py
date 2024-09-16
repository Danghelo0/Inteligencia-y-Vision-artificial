# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 23:02:50 2024

@author: Angel Varela


Búsqueda lineal: Buscando una llave perdida en una habitación
Situación cotidiana: Imagínate que has perdido las llaves en una habitación llena de objetos. La búsqueda lineal implica revisar cada objeto, uno por uno, hasta encontrar las llaves.

Algoritmo: El algoritmo revisa cada objeto en la habitación en secuencia, desde el primero hasta el último, hasta que encuentre las llaves o hasta que termine de revisar todos los objetos.

"""
def busqueda_lineal(objetos, llave_perdida):
    for i, objeto in enumerate(objetos):
        if objeto == llave_perdida:
            return f"Las llaves fueron encontradas en la posición {i}"
    return "Las llaves no están en la habitación"

# Simulación de objetos en la habitación
objetos_en_habitacion = ['libro', 'lámpara', 'taza', 'pluma', 'llave']
resultado = busqueda_lineal(objetos_en_habitacion, 'llave')
print(resultado)
