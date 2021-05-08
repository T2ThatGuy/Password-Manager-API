from flask import jsonify
from app import app

from app.account_actions import AccountActions

#--- Main Page

@app.route('/user')
def user():
    return jsonify({"data": [], "message": "Got to user log in page!"}), 200

# --- Sub Links

@app.route('/user/login')
def login():
    return AccountActions().login()

@app.route('/user/signup')
def signup():
    return AccountActions().signup()

@app.route('/user/update-password')
def update_password():
    return AccountActions().change_password()