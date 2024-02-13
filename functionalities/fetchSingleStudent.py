from flask import Flask, request, jsonify
from utils.db import db, Student, Course, Enrollment

def fetch_single_student(id, internally=False):
    try:
        student = Student.query.get(id)

        if student is None:
            return jsonify({'error': 'Not found'}), 404

        result = {
            "studentId": student.studentId,
            "firstName": student.firstName,
            "lastName": student.lastName,
            "email": student.email
        }

        if internally:
            return result
        return jsonify(result)
    except:
        return jsonify({'error': 'Something went wrong'}), 400