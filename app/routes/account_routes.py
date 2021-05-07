from flask import jsonify
from app import app

from app.account_actions import AccountActions

@app.route('/user/login')
def login():
    return AccountActions().login()

@app.route('/user/signup')
def signup():
    return AccountActions().signup()

@app.route('/user/update-password')
def change_password():
    return AccountActions().change_password()