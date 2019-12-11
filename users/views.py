"""Views Users."""

# Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def login_view(request):
    """ Login View. """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)

        if user:
            login(request, user)
            return redirect('feed')

        else:
            ctx = {'error':'User or pass wrong.'}
            return render(request,"users/login.html",ctx)

    else:
        return render(request,"users/login.html")

def logout(request):
    """ Logout View. """
    logout(request)
    redirect('login')
