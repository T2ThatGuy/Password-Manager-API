from flask import jsonify
from app import app

from app.dashboard_actions import DashboardActions

# --- Main Page

@app.route('/dashboard')
def dashboard():
    return jsonify({"data": [], "message": "Got to dashboard page!"}), 200

# --- Sub Links

@app.route('/dashboard/create-password')
def create_password():
    return DashboardActions().create_password()

@app.route('/dashboard/del-password/<password_id>')
def delete_password(password_id):
    return DashboardActions().delete_password(password_id)

@app.route('/dashboard/change-password/<password_id>')
def change_password(password_id):
    return DashboardActions().change_password(password_id)

@app.route('/dashboard/get-passwords/<user_id>')
def get_passwords(user_id):
    return DashboardActions().get_passwords(user_id)

@app.route('/dashboard/get-password/<password_id>')
def get_password(password_id):
    return DashboardActions().get_password(password_id)
