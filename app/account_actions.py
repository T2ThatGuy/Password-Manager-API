# --- Flask Imports
from flask import request, jsonify

# --- Security Imports
from werkzeug.security import check_password_hash
import uuid, datetime, jwt

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
            token = jwt.encode({'public_id' : user.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=10)}, app.config['SECRET_KEY'])

            data = {
                "id": user.id,
                "username": user.username,
                "public_id": user.public_id,
                "admin": user.admin,
                "token": token
            }

            return jsonify({"data": data, "message": "User signed in successfully"}), 200

        return jsonify({"data": auth, "message": "Could not verify password"}), 401

    # --- Adds the new user to the database and logs them in
    def signup(self):
        data = request.get_json()

        new_user = User(public_id = str(uuid.uuid4()), username=data["username"], password=data['password'], admin = False)
        db.session.add(new_user)
        db.session.commit()

        token = jwt.encode({'public_id' : new_user.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])

        data = {
            "id": new_user.id,
            "username": new_user.username,
            "public_id": new_user.public_id,
            "admin": new_user.admin,
            "token": token
        }

        return jsonify({"data": data, "message": "New user created successfully!"}), 200

    def change_password():
        pass
