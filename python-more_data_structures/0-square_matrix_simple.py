#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Utilisation de la compréhension de liste pour créer une nouvelle matrice
    return [[elem ** 2 for elem in row] for row in matrix]