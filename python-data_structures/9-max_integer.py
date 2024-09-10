#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:  # Si la liste est vide
        return None
    
    # Initialiser le maximum avec le premier élément de la liste
    max_value = my_list[0]
    
    # Parcourir les éléments de la liste et trouver le maximum
    for num in my_list:
        if num > max_value:
            max_value = num
    
    return max_value
