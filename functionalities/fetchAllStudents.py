from flask import Flask, request, jsonify
from utils.db import db, Student, Course, Enrollment

def fetch_all_students():
    try:
        students = Student.query.all()

        result = []
        for student in students:
            result.append({
            "studentId": student.studentId,
            "firstName": student.firstName,
            "lastName": student.lastName,
            "email": student.email
        })

        return jsonify(result)
    except:
        return jsonify({'error': 'Something went wrong'}), 400