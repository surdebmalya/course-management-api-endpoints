from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Student table
class Student(db.Model):
    studentId = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    enrollments = db.relationship('Enrollment', backref='student', cascade='all, delete-orphan')

# Course table
class Course(db.Model):
    courseId = db.Column(db.Integer, primary_key=True)
    courseName = db.Column(db.String(50), nullable=False)
    credits = db.Column(db.Float, nullable=False)
    enrollments = db.relationship('Enrollment', backref='course', cascade='all, delete-orphan')

# Enrollment table
class Enrollment(db.Model):
    studentId = db.Column(db.Integer, db.ForeignKey('student.studentId', ondelete='CASCADE'), primary_key=True)
    courseId = db.Column(db.Integer, db.ForeignKey('course.courseId', ondelete='CASCADE'), primary_key=True)
    marks = db.Column(db.Integer, nullable=True)
