from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import secrets

# initialise SQLAlchemy for database models
db = SQLAlchemy()

# 
def generate_secret_key():
    return secrets.token_hex(24)

def create_app():
    app = Flask(__name__)

    app.config['SECRET KEY'] = generate_secret_key()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    # blueprint registration for auth routes
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint registration for main  routes
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
