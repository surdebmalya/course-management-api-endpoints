# Course management

Language used for backend development: `Python` (flask framework)

### Database Structure
![Database architecture](images/database_image.png)

### Seeding the Database with Mock Data
To seed the database with dummy data from `seed.py` file

To seed the database with mock data just send a request to `/seed` with the `GET` method

The mock data for `Student` table is as follows

![Example of #student](images/student.png)

The mock data for `Course` table is as follows

![Example of #course](images/course.png)

The mock data for `Enrollment` table is as follows

![Example of #enrollment](images/enrollment.png)

### API Codes used

- 200: OK
- 400: Bad request / Invalid argument (invalid request payload)
- 404: Not found
- 409: Conflict response status code indicates a request conflict with the current state of the target resource
- 415: Header is missing

### Project Hierarchy

```
project
    |- main.py
    |- enrollment_utilities
    |    |- enroll.py
    |    |- unenroll.py
    |    |- updateMmarks.py
    |- functionalities
    |    |- createStudent.py
    |    |- fetchSingleStudent.py
    |    |- fetchAllStudent.py
    |    |- deleteSingleStudent.py
    |    |- createCourse.py
    |    |- fetchSingleCourse.py
    |    |- fetchAllCourse.py
    |    |- deleteSingleCourse.py
    |    |- getCourseSingleStudent.py
    |    |- getStudentSingleCourse.py
    |- utils
    |    |- db.py
    |    |- seed.py
    |- instance
    |   |- course_management.db
    |- README.md
    |- images
        |- database_image.png
        |- course.png
        |- student.png
        |- enrollment.png
        |- 1.png
        |- 2.png
        |- 3.png
        |- 4.png
        |- 5.png
        |- 6.png
        |- 7.png
        |- 8.png
        |- 9.png
        |- 10.png
        |- 11.png
        |- 12.png
        |- 13.png
        |- 14.png
        |- 15.png
```

### Testing the functionalities on Postman
**1. Create a student using POST mapping with API endpoint api/students/**
![Example of #1](images/1.png)

**2. Fetch a single student using GET mapping with API endpoint api/students/{id}**
![Example of #2](images/2.png)

**3. Fetch all students using GET mapping with API endpoint api/students/**
![Example of #3](images/3.png)

**4. Delete a specific student using DELETE mapping with API endpoint api/students/{id}**
![Example of #4](images/4.png)

**5. Get courses for a specific student using GET mapping with API endpoint api/students/{id}/courses**
![Example of #5](images/5.png)

**6. Create a course using POST mapping with API endpoint api/courses/**
![Example of #6](images/6.png)

**7. Fetch a single course using GET mapping with API endpoint api/courses/{id}**
![Example of #7](images/7.png)

**8. Fetch all courses using GET mapping with API endpoint api/courses/**
![Example of #8](images/8.png)

**9. Delete a specific course using DELETE mapping with API endpoint api/courses/{id}**
![Example of #9](images/9.png)

**10. Get students for a specific course using GET mapping with API endpoint api/courses/{id}/students**
![Example of #10](images/10.png)

**11 Get the most enrolled course using GET mapping with API endpoint api/courses/most-enrolled**
![Example of #11](images/11.png)

**12 Get the highest marks scored in a specific course by a student using GET mapping with API endpoint api/courses/highest-marks/{courseId}**
![Example of #12](images/12.png)

**13. Enroll a specified student in a course by using POST mapping with API endpoint api/enrollments/enroll. This should add student, and course objects to the Enrollment table**
![Example of #13](images/13.png)

**14. Unenroll a specified student from a course by using DELETE mapping with API endpoint api/enrollments/unenroll**
![Example of #14](images/14.png)

**15. Update marks for a particular student in a specified course by using PUT mapping with API endpoint api/enrollments/updateMarks**
![Example of #15](images/15.png)

### Instruction to run the Application
Install Flask:
```
pip install Flask
```
Install Flask SQLAlchemy:
```
pip install Flask-SQLAlchemy
```
Run the application:
```
python main.py
```
or
```
python3 main.py
```
The application will start running on `http://127.0.0.1:8000/`
