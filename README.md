# University Attendance Portal
University Attendance Portal is a Web Application based on Django which  uses facial recognition API to mark student attendance with student and admin roles. Following stack is used:
- **Django**: Server Side Backend Framework
- **Ajax**: For asynchronous updation of webpages
- **SQLite** Database
- Python, JavaScript, HTML and CSS
- TainWindCSS for templating


## Deployment

Although the application has been Dockerized, but deployment won't be possible via Docker since dlib library of python can't be installed directly via pip install and requires certain dependancies. For installing dlib, follow the following procedure (for Windows):
 

1) Install CMake via: https://cmake.org/download/. Ensure that Windows PATH environment for CMake is added.

2) Install Visual Studio via: https://visualstudio.microsoft.com/visual-cpp-build-tools/. Also install additional packages for C, C++ programming, which is Packages CMake tools for Windows

3) Then, run the following commands on PowerShell:


```bash
  pip install cmake
  pip install dlib
  pip install face-recognition
```


If this still does not work, install dlib source distribution locally in your system from: https://pypi.org/project/dlib/#files. Install 
dlib-19.24.4.tar.gz, extract all the files and then run the following command to install the package to your system global python interpreter:

```bash
  python setup.py install
```

This method works for all Operating Systems.

Once the installation of dlib for the global interpreter is complete, we can start working with the repository:

1. Open Git Bash.
2. Change the current working directory to the location where you want the cloned directory.
3. Run the folloing on the terminal:
```bash
  git clone https://github.com/BlakkTyger/Attendence_app.git
```
4. Enter the Attendence_app directory and install the dependancies from requirements.txt. Using a virtual environment is not recommended since dlib is installed on your global interpreter. Moreover, make sure that you are using your global python interpreter while running the repository.
```bash
  cd Attendence_app
  cd Attendence_app
  pip install -r requirements.txt
```
5. Next, you can run the application using the following commands:

```bash
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
```

This shall complete the setup of the repository. In order to gain admin privileges, you can make a superuser using the following command:
```bash
  python manage.py createsuperuser
```

After setting up the username, email and password for the superuser, you can log in as the admin role by going to /admin.

The superuser account can be used to register a new student, hence you will be able to access as a student and explore the features of the applications



## Features

- **Student Registration**: Admin is able to add a student as the user with user details as well as image of the user in the database. The user details include the courses allotted to the student. The website is supported for multiple user registrations.

- **Admin Login**: Standard Django Admin interface has been used for the purpose of Admin Login as it provides an interactive and comprehensive interface to interact with all models

- **Student Login**: Student is able to log in using his/her credentials allotted by the admin.

- **Class Identification**: On the basis of the date, time and user details, the website shows which course class is taking place for the student. Student can mark attendance only during class timings.

- **Attendance using Face Recognition**: Face Recognition API has been used for the purposes of identify the user, and accordinly mark attendance.

- **Asynchronous image transfer**: AJAX has been used to relay pictures of the student from the webcam to the server at regular intervals to prevent reloading the page every time

- **Attendance history**: Attendance history of a user (for every course separately) is be maintained in the database, a student is able to view his/her attendance history and admin os able to view everyone’s history.

- **Class Tracker**: Due to a comprehensive model architecture, the admin is able to keep a track of which specific class is missed my which student.

- **Responsive Website Design**: The website can be accessable via mostly all devices due to its responsiveness.



## Screenshots

![App Screenshot](https://i.imgur.com/LMg46qd.png?text=App+Screenshot+Here)
Admin Page

![App Screenshot](https://i.imgur.com/ve7iAUo.png?text=App+Screenshot+Here)
User Profile Page 

![App Screenshot](https://i.imgur.com/xPXHK7I.png?text=App+Screenshot+Here)
For Checking which classes are active and marking attendance

![App Screenshot](https://i.imgur.com/pEX0PUB.png?text=App+Screenshot+Here)
For Checking Attendance History



## Implementation Specifications
**Database Structure**

- 5 Model Classes have been implemented:

    1. Course: An object of Course class is defined by attributes name, code and description.
    2. Student: An object of Student class is defined by the attributes first_name, last_name, roll_no, email, phone, date_created and profile_pic. It has a One-To-One relation with User, which means that each User is  uniquely mapped with a student. 
    3. Enrollment: Enrollment Class has Student and Course as its Foreign Keys, and course_attendance and total_classes as its attributes. Each Enrollment is defined by one student enrolling in a particular course. Course_attendance stores the attendance of that student in that particular course and total_classes stores the total classes of the course. Student-Course pair must always be unique together.

    4. ClassSession: ClassSession has Course as its foreign key, and represent a single class of the Course. It has a date-time attribute .

    5. Attendance: Attendance has enrollment and session as foreign keys and a boolean field which represents the presence of the student in that session. Since Enrollment represents Student-Course relationship and Session represencts specific class of the course, Attendance is a relationship between all the 3 classes which can determine the attendance of a student in a specific session of a course.

**Django Signals**

Django Signals are used to communicate between various models and change various attributes and variables on specific events.

1. Signal 1 (update_enrollment_attendance): As soon as a new attendance object is made, attendnace attribute of enrollment is updated to account for total attendance of a student in a course.

2. Signal 2 (update_total_classes): As soon as a session object is created, the total classes of a course are updated.