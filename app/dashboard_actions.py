# --- Flask Imports
from flask import jsonify, request

# --- App Imports
from app.database import db, Password, User
from app import app

class DashboardActions:
    
    def create_password(self, current_user):
        data = request.get_json()

        new_password = Password(
            password_name = data['password_name'], 
            username = data['username'],
            email = data['email'],
            password = data['password'],
            application = data['application'],
            url = data['url'],
            user_id = current_user.id
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
            "user_id": current_user.id
        }

        return jsonify({'data': responseData, 'message': 'The new password has been created successfully'})

    def change_password(user_id, password_id):
        pass

    def delete_password(user_id, password_id):
        pass

    def get_passwords(self, current_user):
        pswArray = []
        response = Password.query.filter_by(user_id = current_user.id)

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
    
    def get_password(user_id, password_id):
        pass
