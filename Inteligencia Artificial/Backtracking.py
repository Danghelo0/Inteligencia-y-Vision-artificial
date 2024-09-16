# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 23:56:55 2024

@author: Angel Varela

Búsqueda en Profundidad con Backtracking: Resolver un sudoku
Situación cotidiana: Quieres resolver un puzzle de Sudoku utilizando un enfoque de búsqueda en profundidad con retroceso cuando encuentras un error.

Algoritmo: El algoritmo intenta colocar números en las celdas vacías y si encuentra un conflicto, retrocede para probar un nuevo número.

"""

def es_valido(tablero, fila, columna, numero):
    # Verificar la fila
    for i in range(9):
        if tablero[fila][i] == numero:
            return False
    # Verificar la columna
    for i in range(9):
        if tablero[i][columna] == numero:
            return False
    # Verificar la subcuadrícula 3x3
    inicio_fila, inicio_columna = 3 * (fila // 3), 3 * (columna // 3)
    for i in range(inicio_fila, inicio_fila + 3):
        for j in range(inicio_columna, inicio_columna + 3):
            if tablero[i][j] == numero:
                return False
    return True

def resolver_sudoku(tablero):
    for fila in range(9):
        for columna in range(9):
            if tablero[fila][columna] == 0:
                for numero in range(1, 10):
                    if es_valido(tablero, fila, columna, numero):
                        tablero[fila][columna] = numero
                        if resolver_sudoku(tablero):
                            return True
                        tablero[fila][columna] = 0
                return False
    return True

# Simulación de Sudoku incompleto
sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

resuelto = resolver_sudoku(sudoku)
print("Sudoku resuelto:" if resuelto else "No se pudo resolver el Sudoku")
print(sudoku)
