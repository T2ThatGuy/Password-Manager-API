from flask_sqlalchemy import SQLAlchemy
from app import app

# --- Database Initialisation
db = SQLAlchemy(app)

# --- User Table & Attributes
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(50), unique = True)
    master_password = db.Column(db.String(128))

    passwords = db.relationship('Password', backref='user', lazy=True)

# --- Password Table & Attributes
class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    password_name = db.Column(db.String(64))
    username = db.Column(db.String(128))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    application = db.Column(db.String(64))
    url = db.Column(db.String(255))
    uid = db.Column(db.String(255))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)