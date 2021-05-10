from flask import jsonify
from app import app

from app.dashboard_actions import DashboardActions
from app.conditions import token_required

# --- Main Page

@app.route('/dashboard')
def dashboard():
    return jsonify({"data": [], "message": "Got to dashboard page!"}), 200

# --- Sub Links

@app.route('/dashboard/create-password', methods=['POST'])
@token_required
def create_password(current_user):
    return DashboardActions().create_password(current_user)

@app.route('/dashboard/del-password/<password_id>')
@token_required
def delete_password(user_id, password_id):
    return DashboardActions().delete_password(user_id, password_id)

@app.route('/dashboard/change-password/<password_id>')
@token_required
def change_password(user_id, password_id):
    return DashboardActions().change_password(user_id, password_id)

@app.route('/dashboard/get-passwords/')
@token_required
def get_passwords(current_user):
    return DashboardActions().get_passwords(current_user)

@app.route('/dashboard/get-password/<password_id>')
@token_required
def get_password(user_id, password_id):
    return DashboardActions().get_password(user_id, password_id)
