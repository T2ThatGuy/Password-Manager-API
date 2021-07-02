from app import app

from app.dashboard_actions import DashboardActions

from flask_jwt_extended import jwt_required

dashboard = DashboardActions()

@app.route('/dashboard/create-password', methods=['POST'])
@jwt_required()
def create_password():
    return dashboard.create_password()

@app.route('/dashboard/del-password', methods=['DELETE'])
@jwt_required()
def delete_password():
    return dashboard.delete_password()

@app.route('/dashboard/change-password', methods=['PUT'])
@jwt_required()
def change_password():
    return dashboard.change_password()

@app.route('/dashboard/get-passwords', methods=['GET'])
@jwt_required()
def get_passwords():
    return dashboard.get_passwords()

@app.route('/dashboard/get-password', methods=['GET'])
@jwt_required()
def get_password():
    return dashboard.get_password()