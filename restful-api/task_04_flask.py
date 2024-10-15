#!/usr/bin/python3
"""Module task_04_flask : Un serveur API simple avec Flask."""
from flask import Flask, jsonify, request  # Import de Flask et des fonctions utiles

# Création de l'application Flask
app = Flask(__name__)

# Dictionnaire pour stocker les utilisateurs (en mémoire)
users = {}


@app.route("/")
def home():
    """
    Route principale "/"
    Renvoie un message de bienvenue.
    """
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """
    Route "/data"
    Renvoie la liste de tous les noms d'utilisateur enregistrés dans le dictionnaire 'users'.
    """
    usernames = list(users.keys())  # Récupérer tous les noms d'utilisateur
    return jsonify(usernames)  # Renvoyer la liste sous forme JSON


@app.route("/status")
def status():
    """
    Route "/status"
    Vérifie l'état de l'API en renvoyant un message "OK".
    """
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """
    Route "/users/<username>"
    Renvoie les informations complètes de l'utilisateur correspondant au 'username' donné.
    Si l'utilisateur n'existe pas, renvoie une erreur 404.
    """
    if username in users:
        return jsonify(users[username])  # Renvoie les infos de l'utilisateur sous forme JSON
    else:
        return jsonify({"error": "User not found"}), 404  # Erreur 404 si l'utilisateur n'existe pas


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Route "/add_user"
    Accepte une requête POST avec des données JSON pour ajouter un nouvel utilisateur.
    Si l'utilisateur est ajouté avec succès, renvoie un message de confirmation et les données de l'utilisateur.
    Si le champ 'username' est manquant, renvoie une erreur 400.
    """
    user_data = request.get_json()  # Récupérer les données JSON envoyées dans la requête

    # Vérifie si 'username' est présent dans les données envoyées
    if "username" not in user_data:
        return jsonify({"error": "Username is required"}), 400  # Erreur 400 si 'username' manquant

    username = user_data["username"]

    # Enregistre les informations de l'utilisateur dans le dictionnaire 'users'
    users[username] = {
        "username": username,
        "name": user_data.get("name"),  # Récupérer le nom (ou None si absent)
        "age": user_data.get("age"),  # Récupérer l'âge (ou None si absent)
        "city": user_data.get("city")  # Récupérer la ville (ou None si absente)
    }

    # Renvoie une réponse 201 (Created) avec les informations de l'utilisateur ajouté
    return jsonify({"message": "User added", "user": users[username]}), 201


# Point d'entrée de l'application
if __name__ == "__main__":
    # Démarre le serveur Flask en mode développement
    app.run()

