from app import db
from models import User, Course

def init_db():
    db.create_all()

    # Add sample users (Admin, Instructor, Student)
    admin = User(name="Admin", role="Admin")
    instructor = User(name="Instructor 1", role="Instructor")
    student = User(name="Student 1", role="Student")
    
    db.session.add(admin)
    db.session.add(instructor)
    db.session.add(student)
    
    db.session.commit()

if __name__ == "__main__":
    init_db()
    
    
