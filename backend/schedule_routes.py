# backend/routes/schedule_routes.py

from flask import Blueprint

schedule_routes = Blueprint('schedule_routes', __name__)

@schedule_routes.route('/')
def list_schedules():
    return "This is the schedule list."
