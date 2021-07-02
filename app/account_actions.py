# --- Flask Imports
from flask import request, jsonify
from flask_jwt_extended.utils import get_jwt_identity

# --- Security Imports
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token, decode_token
from jwt import ExpiredSignatureError, InvalidTokenError
import datetime

# --- App Imports
from app.database import User, db
from app import app

class AccountActions:

    # --- Create an access token that can be returned later
    def create_token(self, user_id, additional_data, duration = 300):
        return create_access_token(identity=str(user_id), additional_claims=additional_data, expires_delta=datetime.timedelta(seconds=duration))

    # --- Verifies and logs in the user if the details are correct whilst returning a token if needed
    def login(self):
        auth = request.authorization

        if not auth or not auth.username or not auth.password:
            return jsonify({"data": [], "message": "Missing authentication data"}), 404

        user = User.query.filter_by(username=auth.username).first()

        if not user:
            return jsonify({"data": auth, "message": "Username not found"}), 404

        if check_password_hash(user.master_password, auth.password):
            token = self.create_token(user.id, {'username': user.username, 'password': user.master_password})

            data = {
                "id": user.id,
                "username": user.username,
                "token": token,
            }

            return jsonify({"data": data, "message": "User signed in successfully"}), 200

        return jsonify({"data": auth, "message": "Could not verify password"}), 401

    # --- Adds the new user to the database and logs them in returning a token if needed
    def signup(self):
        data = request.get_json()

        hashedPass = generate_password_hash(data['password'])

        new_user = User(username=data["username"], master_password = hashedPass)
        db.session.add(new_user)
        db.session.commit()

        token = self.create_token(new_user.id, {'username': new_user.username, 'password': new_user.master_password})

        data = {
            "id": new_user.id,
            "username": new_user.username,
            "token": token
        }

        return jsonify({"data": data, "message": "New user created successfully!"}), 202


    def check_token(self):
        data = request.get_json()
        if not data['token']:
            return jsonify({"data": [], "message": "Missing token"}), 404

        try:
            decode_token(data['token'])
            return jsonify({"data": [], "message": "Token is valid"}), 200
        except ExpiredSignatureError:
            return jsonify({"data": [], "message": "Token is out of date"}), 401
        except InvalidTokenError:
            return jsonify({"data": [], "message": "Token is invalid"}), 401

    def update_password(self):
        data = request.get_json()
        current_id = get_jwt_identity()

        user = User.query.filter_by(id = current_id).first()

        hashedPass = generate_password_hash(data['password'])

        user.master_password = hashedPass

        db.session.commit()

        return jsonify({'data': {'new_token': self.create_token(user.id, {'username': user.username, 'password': user.master_password})}, 'message': 'Account password updated successfully!'}), 200
