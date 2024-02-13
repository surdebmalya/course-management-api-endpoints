from flask import Flask, request, jsonify
import json
from utils.db import db, Student, Course, Enrollment
from functionalities.fetchSingleCourse import *

def get_course_of_a_student(id):
    try:
        student = Student.query.get(id)

        if student is None:
            return jsonify({'error': 'Student is not found'}), 404

        enrollment = Enrollment.query.filter_by(studentId = id).all()

        if enrollment is None:
            return jsonify({'message': 'The student is not enrolled in any course'})

        result = []
        for each in enrollment:
            curr_courseId = each.courseId
            course_data = fetch_single_course(curr_courseId, internally=True)
            result.append(course_data)
        return jsonify(result)
    except:
        return jsonify({'error': 'Something went wrong'}), 400