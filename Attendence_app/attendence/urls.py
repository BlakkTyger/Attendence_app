from . import views
from django.urls import path

urlpatterns = [
    path('signup/', views.sign_up, name = 'sign_up'),
    path('login/', views.log_in, name = 'log_in'),
    path('user-profile/', views.profile, name = 'profile'),
    path('mark-attendence/', views.mark_att, name = 'mark_att'),
    path('attendence-successful', views.att_marked, name = 'att_marked'),
    path('check-attendence/', views.check_att, name = 'check_att'),
]
