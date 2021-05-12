from flask import jsonify
from app import app

from app.dashboard_actions import DashboardActions
from flask_jwt_extended import jwt_required

# --- Main Page

@app.route('/dashboard')
def dashboard():
    return jsonify({"data": [], "message": "Got to dashboard page!"}), 200

# --- Sub Links

@app.route('/dashboard/create-password', methods=['POST'])
@jwt_required()
def create_password():
    return DashboardActions().create_password()

@app.route('/dashboard/del-password', methods=['DELETE'])
@jwt_required()
def delete_password():
    return DashboardActions().delete_password()

@app.route('/dashboard/change-password', methods=['PUT'])
@jwt_required()
def change_password():
    return DashboardActions().change_password()

@app.route('/dashboard/get-passwords')
@jwt_required()
def get_passwords():
    return DashboardActions().get_passwords()

@app.route('/dashboard/get-password')
@jwt_required()
def get_password():
    return DashboardActions().get_password()
