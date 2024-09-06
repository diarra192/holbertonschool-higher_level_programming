#!/usr/bin/python3

import sys

if __name__ == "__main__":
    # Récupérer les arguments
    argv = sys.argv
    argc = len(argv) - 1  # Ne pas compter le nom du script

    # Afficher le nombre d'arguments
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print(f"{argc} arguments:")

    # Afficher chaque argument avec sa position
    for i in range(1, len(argv)):
        print(f"{i}: {argv[i]}")
