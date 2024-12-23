from app import db

# Model for Users (Admin, Instructor, Student)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # Role: Admin, Instructor, Student

# Model for Courses
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    instructor_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Instructor reference
    schedule = db.relationship('Schedule', backref='course', lazy=True)

# Model for Schedules (TimeTable)
class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    day = db.Column(db.String(10), nullable=False)  # Day of the week
    start_time = db.Column(db.String(5), nullable=False)  # e.g., '10:00'
    end_time = db.Column(db.String(5), nullable=False)  # e.g., '12:00'
    room = db.Column(db.String(50), nullable=False)  # Room number or name
