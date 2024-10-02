#!/usr/bin/python3

def enregistrer_dans_fichier_json(mon_dictionnaire, nom_fichier):
    """
    Sérialiser un dictionnaire Python dans un fichier JSON.
    
    :param mon_dictionnaire: Dictionnaire Python à sérialiser
    :param nom_fichier: Nom du fichier dans lequel enregistrer les données JSON
    """
    with open(nom_fichier, 'w', encoding='utf-8') as fichier:
        json.dump(mon_dictionnaire, fichier)


def charger_depuis_fichier_json(nom_fichier):
    """
    Désérialiser un fichier JSON pour recréer un dictionnaire Python.
    
    :param nom_fichier: Nom du fichier à partir duquel lire les données JSON
    :return: Le dictionnaire Python désérialisé depuis le fichier JSON
    """
    with open(nom_fichier, 'r', encoding='utf-8') as fichier:
        return json.load(fichier)

