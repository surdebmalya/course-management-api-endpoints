from flask import Flask, request, jsonify
from utils.db import db
from utils.seed import *
from functionalities.createStudents import *
from functionalities.fetchSingleStudent import *
from functionalities.fetchAllStudents import *
from functionalities.deleteSingleStudent import *
from functionalities.getCourseSingleStudent import *
from functionalities.createCourse import *
from functionalities.fetchSingleCourse import *
from functionalities.fetchAllCourses import *
from functionalities.deleteSingleCourse import *
from functionalities.getStudentSingleCourse import *
from functionalities.mostEnrolled import *
from functionalities.studentsWithHighestMarks import *
from enroll_utilities.enroll import *
from enroll_utilities.unenroll import *
from enroll_utilities.updateMarks import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///course_management.db'
db.init_app(app)

# 0. Seed the database with mock data
@app.route('/seed', methods=['GET'])
def index0():
    return seeding_database()

# 1. Create a student using POST mapping with API endpoint api/students/.
@app.route('/api/students', methods=['POST'])
def index1():
    return create_students()

# 2. Fetch a single student using GET mapping with API endpoint api/students/{id}.
@app.route('/api/students/<int:id>', methods=['GET'])
def index2(id):
    return fetch_single_student(id)

# 3. Fetch all students using GET mapping with API endpoint api/students/.
@app.route('/api/students/', methods=['GET'])
def index3():
    return fetch_all_students()

# 4. Delete a specific student using DELETE mapping with API endpoint api/students/{id}.
@app.route('/api/students/<int:id>', methods=['DELETE'])
def index4(id):
    return delete_single_student(id)

# 5. Get courses for a specific student using GET mapping with API endpoint api/students/{id}/courses.
@app.route('/api/students/<int:id>/courses', methods=['GET'])
def index5(id):
    return get_course_of_a_student(id)

# 6. Create a course using POST mapping with API endpoint api/courses/.
@app.route('/api/courses/', methods=['POST'])
def index6():
    return create_course()

# 7. Fetch a single course using GET mapping with API endpoint api/courses/{id}.
@app.route('/api/courses/<int:id>', methods=['GET'])
def index7(id):
    return fetch_single_course(id)

# 8. Fetch all courses using GET mapping with API endpoint api/courses/.
@app.route('/api/courses/', methods=['GET'])
def index8():
    return fetch_all_courses()

# 9. Delete a specific course using DELETE mapping with API endpoint api/courses/{id}.
@app.route('/api/courses/<int:id>', methods=['DELETE'])
def index9(id):
    return delete_single_course(id)

# 10. Get students for a specific course using GET mapping with API endpoint api/courses/{id}/students.
@app.route('/api/courses/<int:id>/students', methods=['GET'])
def index10(id):
    return get_student_of_a_course(id)

# 11 Get the most enrolled course using GET mapping with API endpoint api/courses/most-enrolled.
@app.route('/api/courses/most-enrolled', methods=['GET'])
def index11():
    return most_enrolled()

# 12 Get the highest marks scored in a specific course by a student using GET mapping with API endpoint api/courses/highest-marks/{courseId}.
@app.route('/api/courses/highest-marks/<int:courseId>', methods=['GET'])
def index12(courseId):
    return students_with_highest_marks(courseId)

# 13. Enroll a specified student in a course by using POST mapping with API endpoint api/enrollments/enroll. This should add student, and course objects to the Enrollment table.
@app.route('/api/enrollments/enroll', methods=['POST'])
def index13():
    return enrolling()

# 14. Unenroll a specified student from a course by using DELETE mapping with API endpoint api/enrollments/unenroll.
@app.route('/api/enrollments/unenroll', methods=['DELETE'])
def index14():
    return unenrolling()

# 15. Update marks for a particular student in a specified course by using PUT mapping with API endpoint api/enrollments/updateMarks.
@app.route('/api/enrollments/updateMarks', methods=['PUT'])
def index15():
    return marks_updation()

if __name__ == '__main__':
    with app.app_context():
        # db.drop_all()
        db.create_all()
    app.run(debug=True, port="8000") #####