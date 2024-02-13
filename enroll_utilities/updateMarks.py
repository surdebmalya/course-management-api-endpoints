from flask import Flask, request, jsonify
from utils.db import db, Student, Course, Enrollment

def marks_updation():
    try:
        data = request.get_json()
        studentId = data["studentId"]
        courseId = data["courseId"]
        try:
            new_marks = data["marks"]
        except:
            return jsonify({'error': 'Payload is missing'}), 400
        enrollment_to_update = Enrollment.query.filter_by(studentId=studentId, courseId=courseId).first()
        if enrollment_to_update:
            enrollment_to_update.marks = new_marks
            db.session.commit()
        else:
            return jsonify({'error': 'Not found'}), 404
        return jsonify({'message': 'Success!'})
    except:
        return jsonify({'error': 'Something went wrong'}), 409