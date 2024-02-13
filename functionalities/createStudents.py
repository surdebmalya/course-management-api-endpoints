from flask import Flask, request, jsonify
from utils.db import db, Student, Course, Enrollment

def create_students():
    try:
        data = request.get_json()
        keys = []
        for i in Student.__table__.columns:
            keys.append(i.key)
        if len(data)==len(keys):
            for key in keys:
                if key not in list(data.keys()):
                    return jsonify({'error': 'Payload is not matching'}), 400
            new_student = Student(
                studentId = data['studentId'],
                firstName = data['firstName'],
                lastName = data['lastName'],
                email = data['email']
            )
            db.session.add(new_student)
            try:
                db.session.commit()
            except:
                return jsonify({'error': 'Something went wrong'}), 409
            return jsonify({'message': 'Success'})
        else:
            return jsonify({'error': 'Payload is missing'}), 400
    except:
        return jsonify({'error': 'Header is missing'}), 415