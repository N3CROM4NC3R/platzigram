"""Views Users."""

# Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators
# Create your views here.

def login_view(request):
    """ Login View. """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)

        # If the user exits redirect to the feed
        if user:
            login(request, user)
            return redirect('feed')

        # Else redirect to the login
        else:
            ctx = {'error':'User or pass wrong.'}
            return render(request,"users/login.html",ctx)

    else:
        return render(request,"users/login.html")


@login_required()
def logout_view(request):
    """ Logout View. """
    logout(request)
    return redirect('login')

def register_view(request):
    """ Register View. """
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        password_repeat = request.POST["repeat_password"]
        if password == password_repeat:

    return render(request,"users/register.html")
