#!/usr/bin/python3
import random
number = random.randint(-10, 10)

# Vérifie si le nombre est positif, négatif ou nul
if number > 0:
    print(f"{number} est positif")
elif number < 0:
    print(f"{number} est négatif")
else:
    print(f"{number} est nul")
