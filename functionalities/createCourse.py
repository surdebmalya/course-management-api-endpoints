from flask import Flask, request, jsonify
from utils.db import db, Student, Course, Enrollment

def create_course():
    try:
        data = request.get_json()
        keys = []
        for i in Course.__table__.columns:
            keys.append(i.key)
        if len(data)==len(keys):
            for key in keys:
                if key not in list(data.keys()):
                    return jsonify({'error': 'Payload is not matching'}), 400
            new_course = Course(
                courseId = data['courseId'],
                courseName = data['courseName'],
                credits = data['credits']
            )
            db.session.add(new_course)
            try:
                db.session.commit()
            except:
                return jsonify({'error': 'Something went wrong'}), 409
            return jsonify({'message': 'Success'})
        else:
            return jsonify({'error': 'Payload is missing'}), 400
    except:
        return jsonify({'error': 'Header is missing'}), 415