from werkzeug.security import generate_password_hash, check_password_hash
from flask import request, jsonify
import uuid, datetime, jwt
from app import app
from app.database import User, db

class AccountActions:

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
            }

            return jsonify({"data": data, "message": "User signed in successfully", "token": token}), 200

        return jsonify({"data": auth, "message": "Could not verify password"}), 401

    def signup(self):
        data = request.get_json()

        hashed_password = generate_password_hash(data["password"], method='sha256')
        new_user = User(public_id = str(uuid.uuid4()), username=data["username"], password=hashed_password, admin = False)
        db.session.add(new_user)
        db.session.commit()

        token = jwt.encode({'public_id' : new_user.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=10)}, app.config['SECRET_KEY'])

        data = {
            "id": new_user.id,
            "username": new_user.username,
            "public_id": new_user.public_id,
            "admin": new_user.admin,
        }

        return jsonify({"data": data, "message": "New user created successfully!", "token": token}), 200

    def change_password():
        pass
