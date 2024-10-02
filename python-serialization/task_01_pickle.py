#!/usr/bin/python3
"""
task_01_pickle.py sérialise et désérialise un objet Python
en utilisant le module pickle
"""
import pickle  # Module pour la sérialisation et désérialisation des objets Python


class CustomObject:
    """
    Objet personnalisé ...

    Méthode __init__

    Args:
        name (str): nom de l'étudiant
        age (int): âge de l'étudiant
        is_student (bool): indique si c'est un étudiant ou non

    Attributs:
        name (str): nom de l'étudiant
        age (int): âge de l'étudiant
        is_student (bool): indique si c'est un étudiant ou non
    """

    name = ""
    age = 0
    is_student = False

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Affiche les attributs d'une instance de cette classe
        """

        obj_dict = self.__dict__

        for key, value in obj_dict.items():
            print(f"{key}: {value}")

    def serialize(self, filename):
        """
        Sérialise l'instance actuelle de la classe et la sauvegarde
        dans le fichier fourni

        Args:
            filename (str): nom du fichier où sauvegarder les données sérialisées

        Returns:
            None
        """

        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Charge et renvoie une instance de
        CustomObject à partir du fichier fourni

        Args:
            filename (str): nom du fichier à charger

        Returns:
            Une instance de CustomObject
        """

        data = ""

        try:
            with open(filename, "rb") as file:
                data = pickle.load(file)
        except:
            return None
        return data

