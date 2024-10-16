from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_jwt_extended.exceptions import NoAuthorizationError, InvalidHeaderError

# Initialisation de l'application Flask
app = Flask(__name__)

# Configuration des clés secrètes : 
# - SECRET_KEY pour Flask
# - JWT_SECRET_KEY pour l'authentification avec JWT
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

# Initialisation de l'authentification basique et JWT
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Liste des utilisateurs avec leur rôle et mot de passe haché
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

# Vérification des identifiants pour Basic Auth
@auth.verify_password
def verify_password(username, password):
    """Vérifie si le nom d'utilisateur et le mot de passe sont corrects."""
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return user  # Retourne l'utilisateur s'il est authentifié

# Route protégée par Basic Auth
@app.route('/basic-protected')
@auth.login_required  # Cette route nécessite une authentification basique
def basic_protected():
    """Accès à une route protégée avec Basic Auth."""
    return "Basic Auth: Access Granted"

# Route de connexion pour générer un token JWT
@app.route('/login', methods=['POST'])
def login():
    """Authentifie un utilisateur et retourne un token JWT."""
    data = request.get_json()  # Récupération des données de la requête JSON
    username = data.get('username')
    password = data.get('password')
    user = users.get(username)

    # Vérifie si l'utilisateur existe et si le mot de passe est correct
    if user and check_password_hash(user['password'], password):
        # Génère un token JWT avec l'identité de l'utilisateur (nom et rôle)
        access_token = create_access_token(identity={"username": username, "role": user['role']})
        return jsonify(access_token=access_token)  # Retourne le token
    return jsonify({"error": "Invalid credentials"}), 401  # Erreur si les identifiants sont incorrects

# Route protégée par JWT
@app.route('/jwt-protected')
@jwt_required()  # Cette route nécessite un token JWT valide
def jwt_protected():
    """Accès à une route protégée avec JWT."""
    return "JWT Auth: Access Granted"

# Route réservée aux administrateurs
@app.route('/admin-only')
@jwt_required()  # Nécessite un token JWT valide
def admin_only():
    """Accès réservé aux administrateurs."""
    current_user = get_jwt_identity()  # Récupère l'identité de l'utilisateur depuis le token JWT

    # Vérifie si l'utilisateur a le rôle 'admin'
    if current_user['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403  # Erreur si l'utilisateur n'est pas admin
    return "Admin Access: Granted"  # Accès accordé si l'utilisateur est admin

# -------------------- GESTION DES ERREURS JWT --------------------

# Gestion de l'erreur : Token manquant ou invalide
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Gestion de l'erreur si le token JWT est manquant ou invalide."""
    return jsonify({"error": "Missing or invalid token"}), 401

# Gestion de l'erreur : Token invalide
@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Gestion de l'erreur si le token JWT est invalide."""
    return jsonify({"error": "Invalid token"}), 401

# Gestion de l'erreur : Token expiré
@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Gestion de l'erreur si le token JWT a expiré."""
    return jsonify({"error": "Token has expired"}), 401

# Gestion de l'erreur : Token révoqué
@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Gestion de l'erreur si le token JWT a été révoqué."""
    return jsonify({"error": "Token has been revoked"}), 401

# Gestion de l'erreur : Besoin d'un token "fresh"
@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Gestion de l'erreur si un token frais est requis."""
    return jsonify({"error": "Fresh token required"}), 401

# -------------------- LANCEMENT DE L'APPLICATION --------------------

# Lancement du serveur Flask
if __name__ == '__main__':
    app.run()

