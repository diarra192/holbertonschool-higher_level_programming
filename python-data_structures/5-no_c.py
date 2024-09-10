#!/usr/bin/python3
def no_c(my_string):
    # On crée une nouvelle chaîne en filtrant les caractères qui ne sont ni 'c' ni 'C'
    new_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string
