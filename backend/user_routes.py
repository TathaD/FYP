# backend/routes/user_routes.py

from flask import Blueprint

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/')
def list_users():
    return "This is the user list."
