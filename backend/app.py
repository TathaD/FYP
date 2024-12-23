# backend/app.py

from flask import Flask
from routes.course_routes import course_routes
from routes.user_routes import user_routes
from routes.schedule_routes import schedule_routes

# Create the Flask application instance
app = Flask(__name__)

# Register the blueprints (routes)
app.register_blueprint(course_routes, url_prefix='/courses')
app.register_blueprint(user_routes, url_prefix='/users')
app.register_blueprint(schedule_routes, url_prefix='/schedule')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

