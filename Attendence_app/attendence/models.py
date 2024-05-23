from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver

class Course(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField()
    
    def __str__(self):
        return f'{self.code}'
    def total_classes(self):
        return ClassSession.objects.filter(course=self).count()



class Student(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20,unique=True)
    email = models.EmailField(max_length=50,unique=True)
    phone = models.CharField(max_length = 10)
    date_created = models.DateTimeField(auto_now_add=True)
    profile_pic = models.ImageField(null = True, blank = True)
    
    def __str__(self):
        return self.roll_no

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    course_attendance = models.PositiveIntegerField(default=0)
    total_classes = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f'{self.student} enrolled in {self.course}'
    
    def update_attendance(self):
        attendance_count = Attendance.objects.filter(enrollment=self, attended=True).count()
        self.course_attendance = attendance_count
        self.total_classes = self.course.total_classes()
        self.save()

class ClassSession(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return f'{self.course.code} - {self.date.strftime("%Y-%m-%d %H:%M:%S")}'

class Attendance(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    session = models.ForeignKey(ClassSession, on_delete=models.CASCADE)
    attended = models.BooleanField(default=False)

    class Meta:
        unique_together = ('enrollment', 'session')

    def __str__(self):
        return f'{self.enrollment.student.roll_no} - {self.session.date.strftime("%Y-%m-%d %H:%M:%S")} - {"Present" if self.attended else "Absent"}'

@receiver(post_save, sender=Attendance)
def update_enrollment_attendance(sender, instance, **kwargs):
    instance.enrollment.update_attendance()

@receiver(post_save, sender=ClassSession)
def update_total_classes(sender, instance, **kwargs):
    enrollments = Enrollment.objects.filter(course=instance.course)
    for enrollment in enrollments:
        enrollment.total_classes = enrollment.course.total_classes()
        enrollment.save()
