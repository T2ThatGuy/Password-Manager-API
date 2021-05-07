from flask import Flask

# --- App Initialization
app = Flask(__name__)

app.config['SECRET_KEY'] = 'Temp Secret Key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

from app.routes import dashboard_routes
from app.routes import account_routes

# --- Database Initialization
from app import database

