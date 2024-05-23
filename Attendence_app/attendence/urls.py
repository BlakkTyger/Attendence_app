from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.log_in, name = 'login'),
    path('login/', views.log_in, name = 'login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name = 'profile'),
    path('select-course/', views.select_course, name = 'select-course'),
    path('check-attendance/', views.check_attendance, name = 'check-attendance'),
    path('video/', views.video, name = 'video'),
    path('recognition/', views.recognition, name='recognition'),
    path('marked/', views.marked, name='marked'),
]
