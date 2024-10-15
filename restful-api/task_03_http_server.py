#!/usr/bin/python3
"""Module task_03_http_server.py : Un serveur HTTP simple."""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Handler qui gère les requêtes HTTP pour l'API."""

    def do_GET(self):
        """Gestion des requêtes GET pour différents points de terminaison."""
        if self.path == '/':
            # Route principale "/"
            # Répond avec un message texte simple.
            self.send_response(200)  # Code de réponse HTTP 200 : OK
            self.send_header('Content-type', 'text/plain')  # Type de contenu texte
            self.end_headers()  # Terminer les en-têtes HTTP
            self.wfile.write(b'Bonjour, ceci est une API simple!')

        elif self.path == '/data':
            # Route "/data"
            # Renvoie un objet JSON avec des informations d'utilisateur.
            self.send_response(200)  # Code 200 : OK
            self.send_header('Content-type', 'application/json')  # Type de contenu JSON
            self.end_headers()
            # Données JSON à envoyer en réponse
            data = {"name": "John", "age": 30, "city": "New York"}
            # Convertir le dictionnaire Python en JSON et l'envoyer au client
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == '/status':
            # Route "/status"
            # Répond avec "OK" pour indiquer que le serveur est en marche.
            self.send_response(200)  # Code 200 : OK
            self.send_header('Content-type', 'text/plain')  # Type de contenu texte
            self.end_headers()
            self.wfile.write(b'OK')

        else:
            # Si l'URL demandée n'est pas définie, renvoie une erreur 404.
            self.send_response(404)  # Code 404 : Not Found
            self.send_header('Content-type', 'application/json')  # Type de contenu JSON
            self.end_headers()
            # Envoyer un message d'erreur au client
            error_message = {"error": "Point de terminaison non trouvé"}
            self.wfile.write(json.dumps(error_message).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    """Fonction qui lance le serveur HTTP."""
    # Configuration de l'adresse et du port du serveur
    server_address = ('', port)  # '' signifie écouter sur toutes les interfaces réseau disponibles
    httpd = server_class(server_address, handler_class)  # Crée une instance du serveur HTTP
    print(f"Le serveur est en cours d'exécution sur le port {port}...")
    httpd.serve_forever()  # Démarre le serveur et attend les requêtes

if __name__ == "__main__":
    # Lancer le serveur si le script est exécuté directement
    run()

