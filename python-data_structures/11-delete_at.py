#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    # Vérifier si l'index est valide (dans la plage des indices de la liste)
    if idx < 0 or idx >= len(my_list):
        return my_list  # Si l'index est invalide, renvoyer la liste inchangée

    # Supprimer l'élément à l'index spécifié
    del my_list[idx]

    # Renvoyer la liste modifiée
    return my_list
