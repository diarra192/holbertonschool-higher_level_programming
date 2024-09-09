def print_reversed_list_integer(my_list=[]):
    if my_list: #Verifie si la liste n'est pas vide
        for i in reversed(my_list):
            print("{:d}".format(i))