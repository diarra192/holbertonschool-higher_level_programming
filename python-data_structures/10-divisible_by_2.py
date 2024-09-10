#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    result = []  # Liste pour stocker les résultats
    for num in my_list:
        # Ajouter True si num est divisible par 2, sinon False
        if num % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result
