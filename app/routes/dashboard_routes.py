from flask import jsonify
from app import app

from app.dashboard_actions import DashboardActions
from flask_jwt_extended import jwt_required
#from app.conditions import token_required

# --- Main Page

@app.route('/dashboard')
def dashboard():
    return jsonify({"data": [], "message": "Got to dashboard page!"}), 200

# --- Sub Links

@app.route('/dashboard/create-password', methods=['POST'])
@jwt_required()
def create_password():
    return DashboardActions().create_password()

@app.route('/dashboard/del-password/<password_id>')
@jwt_required()
def delete_password(password_id):
    return DashboardActions().delete_password(password_id)

@app.route('/dashboard/change-password/<password_id>')
@jwt_required()
def change_password(password_id):
    return DashboardActions().change_password(password_id)

@app.route('/dashboard/get-passwords/')
@jwt_required()
def get_passwords():
    return DashboardActions().get_passwords()

@app.route('/dashboard/get-password/<password_id>')
@jwt_required()
def get_password(password_id):
    return DashboardActions().get_password(password_id)
