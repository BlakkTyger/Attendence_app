from django.contrib import admin
from .models import *

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(ClassSession)
admin.site.register(Attendance)
