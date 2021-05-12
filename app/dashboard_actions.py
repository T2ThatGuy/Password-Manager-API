# --- Flask Imports
from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity

# --- App Imports
from app.database import db, Password, User
from app import app

class DashboardActions:
    
    def create_password(self):
        data = request.get_json()
        user_id = get_jwt_identity()

        new_password = Password(
            password_name = data['password_name'], 
            username = data['username'],
            email = data['email'],
            password = data['password'],
            application = data['application'],
            url = data['url'],
            user_id = user_id
            )

        db.session.add(new_password)
        db.session.commit()

        responseData = {
            "password_name": data['password_name'], 
            "username": data['username'],
            "email": data['email'],
            "password": data['password'],
            "application": data['application'],
            "url": data['url'],
            "user_id": user_id
        }

        return jsonify({'data': responseData, 'message': 'The new password has been created successfully'}), 200

    def change_password(self):
        user_id = get_jwt_identity()
        data = request.get_json()

        if not data or not data['password'] and data['password_id']:
            return jsonify({'data': [], 'message': 'The password is invalid'}), 404

        response = Password.query.filter_by(user_id = user_id, id = data['password_id']).first()

        if not response:
            return jsonify({'data': data, 'message': 'The password could not be found!'}), 404

        response.password = data['password']
        db.session.commit()

        returnData = {
            'id': response.id,
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

        response = Password.query.filter_by(user_id=user_id, id=data['password_id']).first()

        if not response:
            return jsonify({'data': [], 'message': 'Password could not be found!'}), 404

        db.session.delete(response)
        db.session.commit()

        return jsonify({'data': data['password_id'], 'message': 'Password deleted successfully!'}), 200


    def get_passwords(self):
        pswArray = []

        user_id = get_jwt_identity()
        response = Password.query.filter_by(user_id=user_id)

        for psw in response:
            tempDict = {}
            tempDict['id'] = psw.id
            tempDict['password_name'] = psw.password_name
            tempDict['username'] = psw.username
            tempDict['email'] = psw.email
            tempDict['password'] = psw.password
            tempDict['application'] = psw.application
            tempDict['url'] = psw.url

            pswArray.append(tempDict)

        return jsonify({'data': pswArray, 'message': 'Information retrieved succesfully'}), 200
    
    def get_password(self):
        data = request.get_json()
        current_id = get_jwt_identity()

        if not data or not data['password_id']:
            return jsonify({'data': [], 'message': 'Missing password_id'}), 400

        response = Password.query.filter_by(user_id = current_id, id = data['password_id']).first()

        if not response:
            return jsonify({'data': data['password_id'], 'message': 'Password with that id does not exist or you do not have permission to view that password with the current token you have used!'}), 404

        tempDict = {
            'id': response.id,
            'password_name': response.password_name,
            'username': response.username,
            'email': response.email,
            'password': response.password,
            'application': response.application,
            'url': response.url
        }

        return jsonify({'data': tempDict, 'message': 'Information retrieved successfully!'}), 200


