from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Classe personnalisée pour gérer les requêtes HTTP
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    # Gestion des requêtes GET
    def do_GET(self):
        if self.path == '/':  # Page d'accueil
            self.send_response(200)  # Code 200 OK
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Bonjour, c'est une API simple !")

        elif self.path == '/data':  # Endpoint /data pour servir du JSON
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == '/status':  # Endpoint /status
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            status = {"status": "OK"}
            self.wfile.write(json.dumps(status).encode('utf-8'))

        elif self.path == '/info':  # Endpoint /info
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            info = {"version": "1.0", "description": "Une API simple créée avec http.server"}
            self.wfile.write(json.dumps(info).encode('utf-8'))

        else:  # Gestion des erreurs 404 pour tout autre point de terminaison
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_message = {"error": "Point de terminaison non trouvé"}
            self.wfile.write(json.dumps(error_message).encode('utf-8'))

# Fonction pour démarrer le serveur sur le port 8000
def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Serveur démarré sur le port {port}. Visitez http://localhost:{port}")
    httpd.serve_forever()

# Démarrage du serveur si le fichier est exécuté directement
if __name__ == '__main__':
    run()

