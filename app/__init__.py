from flask_jwt_extended import JWTManager
from flask import Flask

# --- App Initialization & Configs
app = Flask(__name__)

app.config['SECRET_KEY'] = 'Temp Secret Key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

app.config['JWT_SECRET_KEY'] = 'random test string'
jwt = JWTManager(app)

# --- Application Route Imports
from app.routes import dashboard_routes
from app.routes import account_routes

# --- Database Initialization
from app import database

