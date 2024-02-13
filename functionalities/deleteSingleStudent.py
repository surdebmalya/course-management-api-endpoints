from flask import Flask, request, jsonify
from utils.db import db, Student, Course, Enrollment

def delete_single_student(id):
    record_to_delete = Student.query.get(id)
    if record_to_delete:
        db.session.delete(record_to_delete)
        db.session.commit()
        return jsonify({'message': 'Success'})
    else:
        return jsonify({'error': 'Something went wrong'}), 404