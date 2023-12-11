from flask import Blueprint
from . import db

main = Blueprint('main', __name__)

@main.route('/signup')
def signup():
    return 'Signup'

@main.route('/login')
def login():
    return 'Login'

@main.route('/logout')
def logout():
    return 'Logout'
