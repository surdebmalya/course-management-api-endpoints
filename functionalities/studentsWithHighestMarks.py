from flask import Flask, request, jsonify
from utils.db import db, Student, Course, Enrollment
from functionalities.getStudentSingleCourse import *
from functionalities.fetchSingleStudent import *

def students_with_highest_marks(courseId):
    try:
        max_marks, list_of_student_ids = get_student_of_a_course(courseId, from_students_with_highest_marks=True)
        if max_marks==-1:
            return jsonify({'message': 'No marks are uploaded'})
        result = {"max_marks": max_marks, "students": []}
        for student_id in list_of_student_ids:
            result['students'].append(fetch_single_student(student_id, internally=True))
        return jsonify(result)
    except:
        return jsonify({'error': 'Something went wrong'}), 400