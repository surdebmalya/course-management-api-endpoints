from flask import Flask, request, jsonify
from utils.db import db, Student, Course, Enrollment

def unenrolling():
    try:
        data = request.get_json()
        studentId = data["studentId"]
        courseId = data["courseId"]
        enrollment_to_delete = Enrollment.query.filter_by(studentId=studentId, courseId=courseId).first()
        if enrollment_to_delete:
            db.session.delete(enrollment_to_delete)
            db.session.commit()
        else:
            return jsonify({'error': 'Not found'}), 404
        return jsonify({'message': 'Success!'})
    except:
        return jsonify({'error': 'Something went wrong'}), 409