from app import app

from app.account_actions import AccountActions

from flask_jwt_extended import jwt_required

account = AccountActions()

@app.route('/user/token-verify')
def check_token():
    return account.check_token()

@app.route('/user/login', methods = ['GET'])
def login():
    return account.login()

@app.route('/user/signup', methods = ['POST'])
def signup():
    return account.signup()

@app.route('/user/update-password', methods=['PUT'])
@jwt_required()
def update_password():
    return account.update_password()
