from flask import Flask, request, jsonify
from utils.db import db, Student, Course, Enrollment

def fetch_single_course(id, internally=False):
    try:
        course = Course.query.filter_by(courseId = id).all()
        if course[0] is None:
            return jsonify({'error': 'Not found'}), 404

        result = {
            "courseId": course[0].courseId,
            "courseName": course[0].courseName,
            "credits": course[0].credits
        }
        if internally:
            return result
        return jsonify(result)
    except:
        return jsonify({'error': 'Something went wrong'}), 400