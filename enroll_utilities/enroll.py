from flask import Flask, request, jsonify
from utils.db import db, Student, Course, Enrollment

def enrolling():
    try:
        data = request.get_json()
        studentId = data["studentId"]
        courseId = data["courseId"]
        try:
            marks = data["marks"]
        except:
            marks = None
        new_enrollment = Enrollment(
            studentId = studentId,
            courseId = courseId,
            marks = marks
        )
        db.session.add(new_enrollment)
        try:
            db.session.commit()
        except:
            return jsonify({'error': 'Something went wrong'}), 409
        return jsonify({'message': 'Success!'})
    except:
        return jsonify({'error': 'Something went wrong'}), 409