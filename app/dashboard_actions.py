# --- Flask Imports
from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity

# --- App Imports
from app.database import db, Password, User
from app import app

import uuid

class DashboardActions:

    def create_password(self):
        data = request.get_json()
        user_id = get_jwt_identity()

        if not 'uid' in data:
            uid = uuid.uuid4()

        new_password = Password(
            password_name = data['password_name'], 
            username = data['username'],
            email = data['email'],
            password = data['password'],
            application = data['application'],
            url = data['url'],
            user_id = user_id,
            uid = data['uid'] if 'uid' in data else str(uid)
        )

        db.session.add(new_password)
        db.session.commit()

        responseData = {
            "uid": uid,
            "password_name": data['password_name'], 
            "username": data['username'],
            "email": data['email'],
            "password": data['password'],
            "application": data['application'],
            "url": data['url']
        }

        return jsonify({'data': responseData, 'message': 'The new password has been created successfully'}), 202

    def change_password(self):
        user_id = get_jwt_identity()
        data = request.get_json()

        if not data or not data['password'] and data['password_id']:
            return jsonify({'data': [], 'message': 'The password is invalid'}), 404

        response = Password.query.filter_by(user_id = user_id, uid = data['password_id']).first()

        if not response:
            return jsonify({'data': data, 'message': 'The password could not be found!'}), 404

        response.password = data['password']
        db.session.commit()

        returnData = {
            'uid': response.uid,
            'password_name': response.password_name,
            'username': response.username,
            'email': response.email,
            'password': response.password,
            'application': response.application,
            'url': response.url
        }

        return jsonify({'data': returnData, 'message': 'The password has been changed successfully!'}), 200

    def delete_password(self):
        data = request.get_json()
        user_id = get_jwt_identity()

        if not data or not data['password_id']:
            return jsonify({'data': [], 'message': 'Data inputed is invalid!'}), 400

        response = Password.query.filter_by(user_id=user_id, uid=data['password_id']).first()

        if not response:
            return jsonify({'data': [], 'message': 'Password could not be found!'}), 404

        db.session.delete(response)
        db.session.commit()

        return jsonify({'data': data['password_id'], 'message': 'Password deleted successfully!'}), 200

    def get_passwords(self):
        psw_array = []

        user_id = get_jwt_identity()
        response = User.query.filter_by(id=user_id).first()

        passwords = response.passwords

        for psw in passwords:
            temp_dict = {
                'id': psw.id,
                'password_name': psw.password_name,
                'username': psw.username,
                'email': psw.email,
                'password': psw.password,
                'application': psw.application,
                'url': psw.url
            }

            psw_array.append(temp_dict)

        return jsonify({'data': psw_array, 'message': 'tbd'}), 200

    def get_password(self):
        data = request.get_json()
        user_id = get_jwt_identity()

        response = Password.query.filter_by(uid=data['password_id'], user_id=user_id).first()

        if not response:
            return jsonify({'data': [], 'message': 'Password could not be found!'}), 404

        else:
            returnData = {
                'uid': response.uid,
                'password_name': response.password_name,
                'username': response.username,
                'email': response.email,
                'password': response.password,
                'application': response.application,
                'url': response.url
            }

            return jsonify({'data': returnData, 'message': 'Password found!'}), 200

