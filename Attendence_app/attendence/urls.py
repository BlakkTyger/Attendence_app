from . import views
from django.urls import path, include

urlpatterns = [
    path('login/', views.log_in, name = 'log_in'),
    path('user-profile/', views.profile, name = 'profile'),
    path('mark-attendence/', views.mark_att, name = 'mark_att'),
    path('attendence-successful', views.att_marked, name = 'att_marked'),
    path('check-attendence/', views.check_att, name = 'check_att'),
    path('mark/', views.mark, name = 'mark'),
    path('logout/', views.user_logout, name='logout'),
    path('att_marked/', views.att_marked, name='marked'),
    path('att-marked-final/', views.att_marked_final, name='att-marked-final'),
]
