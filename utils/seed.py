from flask import jsonify
from utils.db import db, Student, Course, Enrollment

def seeding_database():
    student_details = [
        {
            'studentId': 1234, 
            'firstName': 'Arshia', 
            'lastName': 'Chaudhuri', 
            'email': 'chaudhuri.arshia@gmail.com'
        },
        {
            'studentId': 1235, 
            'firstName': 'Debmalya', 
            'lastName': 'Sur', 
            'email': 'sur.debmalya@gmail.com'
        },
        {
            'studentId': 1236, 
            'firstName': 'Arjun', 
            'lastName': 'Rampal', 
            'email': 'rampal.arjun@gmail.com'
        },
        {
            'studentId': 1237, 
            'firstName': 'Surya', 
            'lastName': 'Yadav', 
            'email': 'yadav.surya@gmail.com'
        },
    ]

    # checking for the duplication of the student id
    try:
        for student_data in student_details:
                new_student = Student(
                    studentId = student_data['studentId'],
                    firstName = student_data['firstName'],
                    lastName = student_data['lastName'],
                    email = student_data['email']
                    )
                db.session.add(new_student)

        db.session.commit()
    except:
        return jsonify({'error': 'Either student id or email already exist'}), 409

    course_details = [
        {
            'courseId': 456,
            'courseName': 'Operating System',
            'credits': 9.5
        },
        {
            'courseId': 457,
            'courseName': 'Database Management',
            'credits': 8.5
        },
    ]

    # checking for the duplication of the course id
    try:
        for course_data in course_details:
                new_course = Course(
                    courseId = course_data['courseId'],
                    courseName = course_data['courseName'],
                    credits = course_data['credits']
                    )
                db.session.add(new_course)

        db.session.commit()
    except:
        return jsonify({'error': 'Course ID should be unique for each course!'}), 409

    enrollment_details = [
        {
            "studentId": 1234,
            "courseId": 456,
            "marks": 95
        },
        {
            "studentId": 1235,
            "courseId": 456,
            "marks": 89
        },
        {
            "studentId": 1235,
            "courseId": 457,
            "marks": 91
        }
    ]
    
    # checking for the duplication of the course id
    try:
        for enrollment_detail in enrollment_details:
                new_enrollment = Enrollment(
                    studentId = enrollment_detail['studentId'],
                    courseId = enrollment_detail['courseId'],
                    marks = enrollment_detail['marks']
                    )
                db.session.add(new_enrollment)

        db.session.commit()
    except:
        return jsonify({'error': 'Something went wrong for Enrollment model creation'}), 409

    return jsonify({'message': 'Success'})