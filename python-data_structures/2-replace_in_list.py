#!/usr/bin/python3
def replace_in_list(my_list, idx, elemet):
    if idx < 0 or idx >= len(my_list):
        return my_list #ne modifie rien et returne la liste original
    my_list[idx] = element 
    return my_list
        