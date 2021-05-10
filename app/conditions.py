from flask import request, jsonify
from functools import wraps
from app import app
import jwt

from app.database import User

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'data': [], 'message': 'Access token is missing'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = User.query.filter_by(public_id = data['public_id']).first()

        except Exception as e:
            print(e)
            return jsonify({'data': [], 'message': 'Token is invalid'}), 401

        return f(current_user, *args, **kwargs)

    return decorated
