from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length = 10)
    description = models.TextField()
    class_1 = models.DateTimeField(blank = True, null = True)
    class_2 = models.DateTimeField(blank = True, null = True)
    class_3 = models.DateTimeField(blank = True, null = True)
    class_4 = models.DateTimeField(blank = True, null = True)
    class_5 = models.DateTimeField(blank = True, null = True)
    total_classes = models.PositiveIntegerField(blank = True)

    def __str__(self):
        return self.code

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20,unique=True)
    email = models.EmailField(max_length=50,unique=True)
    phone = models.CharField(max_length = 10)
    date_created = models.DateTimeField(auto_now_add=True)
    '''
    courses = {
        "MTH113": "MTH113: Linear Algebra",
        "MTH114": "MTH114: Ordinary Differential Equations",
        "ESO207": "ESO207: Data Structures and Algorithms",
        "CS771": "CS771: Introduction to Machine Learning",
        "MSO205": "MSO205: Introduction to Probability Theory",
        "DMS625": "DMS625: Introduction to Stochastic Processes and their Applications",
        "PHY431": "PHY431: Quantum Mechanics I",
        "PHY432": "PHY432: Quantum Mechanics II",
        "EE798I": "EE798I: Nanophotonics",
        "EE798Z": "EE798Z: Mathematical Engineering and Physics using Machine Learning"
    }
    courses = [(k, v) for k, v in courses.items()]'''
 
    '''course_1 = models.CharField(max_length=6, choices=courses, null=True, blank = True)
    attendence_course_1 = models.IntegerField(null=True, blank = True)
    course_2 = models.CharField(max_length=6, choices=courses, null=True, blank = True)
    attendence_course_2 = models.IntegerField(null=True, blank = True)
    course_3 = models.CharField(max_length=6, choices=courses, null=True, blank = True)
    attendence_course_3 = models.IntegerField(null=True, blank = True)
    course_4 = models.CharField(max_length=6, choices=courses, null=True, blank = True)
    attendence_course_4 = models.IntegerField(null=True, blank = True)
    course_5 = models.CharField(max_length=6, choices=courses, null=True, blank = True)
    attendence_course_5 = models.IntegerField(null=True, blank = True)
    course_6 = models.CharField(max_length=6, choices=courses, null=True, blank = True)
    attendence_course_6 = models.IntegerField(null=True, blank = True)
    course_7 = models.CharField(max_length=6, choices=courses, null=True, blank = True)
    attendence_course_7 = models.IntegerField(null=True, blank = True)
    course_8 = models.CharField(max_length=6, choices=courses, null=True, blank = True)
    attendence_course_8 = models.IntegerField(null=True, blank = True)'''

    #courses = models.ManyToManyField(Course)


    def __str__(self):
        return self.roll_no

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    attendance = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f'{self.student} enrolled in {self.course}'

