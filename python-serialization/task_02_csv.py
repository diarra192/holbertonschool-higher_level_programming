#!/usr/bin/python3
"""
task_02_csv.py lecture de données à partir d'un format (CSV)
et conversion en un autre format (JSON)
"""
import csv
import json


def convert_csv_to_json(csv_file):
    """
    Convertit un fichier CSV en JSON

    Args:
        csv_file (str): nom du fichier CSV

    Returns:
        bool: True si la conversion a réussi, False sinon
    """

    data = []

    try:
        # Ouvre et lit le fichier CSV
        with open(csv_file, encoding="utf-8") as csvfile:
            csv_read = csv.DictReader(csvfile)  # Lit le CSV en tant que dictionnaire
            for row in csv_read:
                data.append(row)  # Ajoute chaque ligne du CSV à la liste de données

    except FileNotFoundError:
        # Retourne False si le fichier CSV est introuvable
        return False

    try:
        # Écrit les données dans un fichier JSON
        with open("data.json", "w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, ensure_ascii=False, indent=4)  # Conversion en JSON avec formatage
    except:
        # Retourne False en cas de problème lors de l'écriture du fichier JSON
        return False
    return True

