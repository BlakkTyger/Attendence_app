from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def log_in(request):
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

@login_required(login_url='login')
def profile(request):
    return render(request, 'profile.html')

@login_required(login_url='login')
def mark_att(request):
    return render(request, 'mark-att.html')

@login_required(login_url='login')
def att_marked(request):
    return render(request, 'att-marked.html')

@login_required(login_url='login')
def check_att(request):
    return render(request, 'check-att.html')
