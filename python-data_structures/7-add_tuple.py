#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Ajouter des 0 pour les éléments manquants dans les tuples
    a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    a2 = tuple_a[1] if len(tuple_a) > 1 else 0
    b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b2 = tuple_b[1] if len(tuple_b) > 1 else 0

    # Retourner le résultat de l'addition des deux tuples
    return (a1 + b1, a2 + b2)
