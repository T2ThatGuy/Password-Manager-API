from flask_sqlalchemy import SQLAlchemy
from app import app

# --- Database Initialization
db = SQLAlchemy(app)

# --- User Table & Attributes
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    public_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(128))

    admin = db.Column(db.Boolean)

# --- Password Table & Attributes
class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    password_name = db.Column(db.String(64))
    username = db.Column(db.String(128))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    application = db.Column(db.String(64))
    url = db.Column(db.String(255))

    user_id = db.Column(db.Integer)