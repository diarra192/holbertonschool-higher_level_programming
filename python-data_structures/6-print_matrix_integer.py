#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        # Utiliser str.format() pour chaque élément de la ligne
        print(" ".join("{:d}".format(num) for num in row))
