# --- Flask Imports
from flask import request, jsonify
from flask_jwt_extended.utils import get_jwt_identity

# --- Security Imports
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token
import uuid, datetime

# --- App Imports
from app.database import User, db
from app import app

class AccountActions:

    # --- Verifies and logs in the user if the details are correct
    def login(self):
        auth = request.authorization

        if not auth or not auth.username or not auth.password:
            return jsonify({"data": [], "message": "Missing authentication data"}), 404

        user = User.query.filter_by(username=auth.username).first()

        if not user:
            return jsonify({"data": auth, "message": "Username not found"}), 404

        if check_password_hash(user.password, auth.password):
            expires = datetime.timedelta(days=7)
            token = create_access_token(identity=str(user.id), expires_delta=expires)

            data = {
                "id": user.id,
                "username": user.username,
                "public_id": user.public_id,
                "admin": user.admin,
                "token": token,
                "user_password": user.password
            }

            return jsonify({"data": data, "message": "User signed in successfully"}), 200

        return jsonify({"data": auth, "message": "Could not verify password"}), 401

    # --- Adds the new user to the database and logs them in
    def signup(self):
        data = request.get_json()

        hashedPass = generate_password_hash(data['password'])

        new_user = User(public_id = str(uuid.uuid4()), username=data["username"], password = hashedPass, admin = False)
        db.session.add(new_user)
        db.session.commit()

        expires = datetime.timedelta(days=7)
        token = create_access_token(identity=str(new_user.id), expires_delta=expires)

        data = {
            "id": new_user.id,
            "username": new_user.username,
            "public_id": new_user.public_id,
            "admin": new_user.admin,
            "token": token
        }

        return jsonify({"data": data, "message": "New user created successfully!"}), 200

    def change_password(self):
        data = request.get_json()
        current_id = get_jwt_identity()

        user = User.query.filter_by(id = current_id).first()

        hashedPass = generate_password_hash(data['password'])

        user.password = hashedPass

        db.session.commit()

        return jsonify({'data': [], 'message': 'Account password updated successfully!'})



