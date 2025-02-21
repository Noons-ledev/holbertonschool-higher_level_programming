#!/usr/bin/python3
"""
We will use flask with jwt werkzeug ans flaskhttpauth
"""
from flask import Flask, jsonify, request
import jwt
from flask_jwt_extended import JWTManager, \
    create_access_token, jwt_required, get_jwt_identity, get_jwt
import requests
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
jwt = JWTManager(app)
auth = HTTPBasicAuth()
app.config['JWT_SECRET_KEY'] = "MykeyforJWT1234"

users = {
    "user1": {"username": "user1", "password":
              generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password":
               generate_password_hash("password"), "role": "admin"}
}


@app.route('/basic-protected')
@auth.login_required
def basic_login():
    return "Basic Auth: Access Granted"


@auth.verify_password
def verify_password(username, password):
    if username in users and \
       check_password_hash(users[username]['password'], password):
        return username
    else:
        return None, 401


@app.route('/login', methods=['POST'])
@auth.login_required
def login():
    user_name = request.json.get('username')
    user_pwd = request.json.get('password')
    islogged = verify_password(user_name, user_pwd)
    if islogged is not None:
        access_token = create_access_token(identity=user_name,
                                           additional_claims={
                                               'role':
                                                   users[user_name]['role']})
        return jsonify(access_token=access_token)
    return 401


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


@app.route('/admin-only')
@jwt_required()
def is_admin():
    current_user = get_jwt_identity()
    claim = get_jwt()
    user_role = claim.get('role')
    if user_role == 'admin':
        return "Admin Access: Granted"
    else:
        return jsonify({"error": "Admin access required"}), 403


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
