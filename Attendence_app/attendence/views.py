from django.shortcuts import render
from django.http import HttpResponse

def sign_up(request):
    return render(request, 'signup.html')

def log_in(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

def mark_att(request):
    return render(request, 'mark-att.html')

def att_marked(request):
    return render(request, 'att-marked.html')

def check_att(request):
    return render(request, 'check-att.html')
