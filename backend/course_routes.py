# backend/routes/course_routes.py

from flask import Blueprint

# Define the blueprint for course routes
course_routes = Blueprint('course_routes', __name__)

# Define a route under the blueprint
@course_routes.route('/')
def list_courses():
    return "List of courses"
