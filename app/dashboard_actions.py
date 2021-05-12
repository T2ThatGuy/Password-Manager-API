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

        return jsonify({'data': responseData, 'message': 'The new password has been created successfully'})

    def change_password(password_id):
        pass

    def delete_password(password_id):
        pass

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

        return jsonify({'data': pswArray, 'message': 'Information retrieved succesfully'})
    
    def get_password(password_id):
        pass
