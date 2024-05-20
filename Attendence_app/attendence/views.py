from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def sign_up(request):
    return render(request, 'signup.html')


def log_in(request):
    
    return render(request, 'login.html')

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def mark_att(request):
    return render(request, 'mark-att.html')

@login_required
def att_marked(request):
    return render(request, 'att-marked.html')

@login_required
def check_att(request):
    return render(request, 'check-att.html')
