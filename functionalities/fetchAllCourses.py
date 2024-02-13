from flask import Flask, request, jsonify
from utils.db import db, Student, Course, Enrollment

def fetch_all_courses():
    try:
        courses = Course.query.all()

        result = []
        for course in courses:
            result.append({
            "courseId": course.courseId,
            "courseName": course.courseName,
            "credits": course.credits
        })

        return jsonify(result)
    except:
        return jsonify({'error': 'Something went wrong'}), 400