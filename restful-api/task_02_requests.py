import requests  # Pour envoyer des requêtes HTTP
import csv       # Pour écrire dans un fichier CSV

# Fonction pour récupérer les posts et imprimer les titres
def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)  # Envoi de la requête GET

    # Vérifie si la requête a réussi
    print(f"Code d'état : {response.status_code}")
    if response.status_code == 200:
        posts = response.json()  # Analyse du contenu JSON
        # Parcourir et afficher les titres
        for post in posts:
            print(post['title'])
    else:
        print("Échec de la récupération des messages.")

# Fonction pour récupérer les posts et les enregistrer dans un fichier CSV
def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)  # Envoi de la requête GET

    if response.status_code == 200:
        posts = response.json()  # Analyse du contenu JSON

        # Préparation des données sous forme de liste de dictionnaires
        data = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']}
            for post in posts
        ]

        # Écriture des données dans un fichier CSV
        with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()  # Écrire les en-têtes de colonnes
            writer.writerows(data)  # Écrire les lignes de données
        print("Données enregistrées dans posts.csv.")
    else:
        print("Échec de la récupération des messages.")

