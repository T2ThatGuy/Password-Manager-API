from flask import jsonify
from app import app

@app.route('/dashboard')
def dashboard():
    return jsonify({"data": [], "message": "Got to dashboard page!"}), 200