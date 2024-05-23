from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils import timezone
from django.core.files.base import ContentFile
import time
import datetime
from django.views.decorators.csrf import csrf_exempt

import numpy as np
import base64
from io import BytesIO
from PIL import Image
import face_recognition

from pathlib import Path
import os


from .models import *
from .decorators import unauth_user, allowed_users

def log_in(request):
    #if request.user.is_authenticated:
    #    return redirect('log_in')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password = password)

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.info(request, "Username or  password is incorrect")

    return render(request, 'login.html')

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')

'''@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def admin_page(request):
    return render(request, 'admin.html')'''

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def profile(request):
    first_name = request.user.student.first_name
    last_name = request.user.student.last_name
    roll_no = request.user.student.roll_no
    email = request.user.student.email

    student = request.user.student
    enrollments = Enrollment.objects.filter(student=student)
    attendance_records = Attendance.objects.filter(enrollment__in=enrollments)

    context = {
        "first_name": first_name,
        "last_name": last_name,
        "roll_no": roll_no,
        "email": email,
        "courses": enrollments,
        "attendance": attendance_records
    }
    return render(request, 'profile.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def video(request):
    if request.method == 'POST':
        course = request.POST.get('course')
        request.session['course'] = course
        return render(request, 'video.html', {'course': course})


@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def select_course(request):
    now = timezone.now()
    ongoing_sessions = ClassSession.objects.filter(date__lte=now, date__gt=now - timezone.timedelta(hours=1))
    context = {"sesh": ongoing_sessions}
    return render(request, 'select-course.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def check_attendance(request):
    student = request.user.student
    enrollments = Enrollment.objects.filter(student=student)
    attendance_records = Attendance.objects.filter(enrollment__in=enrollments)
    c = []
    cnt = 1
    for x  in enrollments:
        #percent = (x.course_attendance/x.total_classes)*100
        c.append({"Sno":cnt,"0":x.course.name, "1":x.course_attendance, "2":x.total_classes, "3":0})
        cnt+=1

    context = {'info': c}
    return render(request, 'check-attendence.html',context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def recognition(request):
    pic_name = request.user.student.profile_pic.url.split('/')[-1]
    BASE_DIR = Path(__file__).resolve().parent.parent
    dir_path = os.path.join(BASE_DIR, "static")
    path = dir_path + "/img/"+pic_name
    
    # Load known face(s) and encode
    known_image = face_recognition.load_image_file(path)
    known_face_encoding = face_recognition.face_encodings(known_image)[0]

    #--------------------------------------------------------------
    #--------------------------------------------------------------
    
    if request.method == 'POST':
        image_data = request.POST.get('image')
        if image_data.startswith('data:image'):
            image_data = image_data.split(',')[1]
        image_data = base64.b64decode(image_data)
        image = Image.open(BytesIO(image_data))
        image = image.convert('RGB')
        image_array = np.array(image)
        print("CHeckpoint 1")
        print(image_array.shape)
        print("CHeckpoint 1.1")
        captured_face_encodings = face_recognition.face_encodings(image_array)
        print("CHeckpoint 2")
        print(captured_face_encodings)
        print("CHeckpoint 3")
        should_stop = False
        if captured_face_encodings:
            match = face_recognition.compare_faces([known_face_encoding], captured_face_encodings[0])
            print("CHeckpoint 4")
            if match[0]:
                should_stop = True
                print("CHeckpoint 5")
                return JsonResponse({'status': 'success', 'should_stop': should_stop, 'redirect_url': '/marked/'})
            else:
                print("CHeckpoint 6")
                #return JsonResponse({'message': 'Face not recognized.'})
                return JsonResponse({'status': 'fail'})
        else:
            print("CHeckpoint 7")
            #return JsonResponse({'message': 'No face detected.'})
            return JsonResponse({'status': 'fail'})

    print("CHeckpoint 8")
    return JsonResponse({'status': 'fail'})
    #return JsonResponse({'message': 'Invalid request.'})


@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def marked(request):
    student = request.user.student
    session = request.session.get('course')
    context = {"sesh":session}
    course_code = session.split(' - ')[0]
    print(course_code)
    format = "%Y-%m-%d %H:%M:%S"
    dt = session.split(' - ')[1]
    datetime_str = datetime.datetime.strptime(dt, format) 
    print(datetime_str)
    course = get_object_or_404(Course, code = course_code)
    enroll = get_object_or_404(Enrollment, student = student, course = course)
    sesh = get_object_or_404(ClassSession, course = course, date = datetime_str)

    Attendance.objects.create(enrollment = enroll, session = sesh, attended = True)
    



    
    return render(request, 'marked.html',context)