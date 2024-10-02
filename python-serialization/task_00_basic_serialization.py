#!/usr/bin/python3
"""
task_00_basic_serialization.py module qui sérialise un dictionnaire Python
dans un fichier JSON et désérialise le fichier JSON pour
recréer le dictionnaire Python
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Sérialise les données et les sauvegarde dans un fichier

    Args:
        data (object): objet Python à sérialiser
        filename (str): nom du fichier où sauvegarder les données sérialisées
    """

    with open(filename, "w") as file:
        json.dump(data, file)  # Sérialisation et écriture dans le fichier


def load_and_deserialize(filename):
    """
    Charge et désérialise les données à partir d'un fichier spécifié

    Args:
        filename (str): nom du fichier d'où charger les données

    Returns:
        Retourne un objet Python avec les données JSON désérialisées
    """

    with open(filename, "r") as file:
        return json.load(file)  # Chargement et désérialisation du fichier JSON

