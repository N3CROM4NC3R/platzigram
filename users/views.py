"""Views Users."""

# Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Local
from users.models import Profile

# Create your views here.


@login_required
def update_profile(request):
    """ Update a user's profile view. """
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        website = request.POST["website"]
        biography = request.POST["biography"]

        request.user.first_name = first_name
        request.user.last_name = last_name
        request.user.email = email
        request.user.profile.website = website
        request.user.profile.biography = biography
        request.user.save()
        return redirect('feed')

    ctx = {
        "user"   : request.user,
        "profile": request.user.profile
    }
    return render(request,"users/update_profile.html",ctx)

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
        email = request.POST["email"]
        password = request.POST["password"]
        password_repeat = request.POST["repeat_password"]

        if password != password_repeat:
            ctx = {
                "error":"Passwords not match"
            }
            return render(request,"users/register.html",ctx)

        try:
            user = User.objects.create_user(username=username,email=email,password=password)
        except IntegrityError as ie:
            ctx = {
                "error":"User exists",
            }
            return render(request,"users/register.html",ctx)


        user.first_name = request.POST["first_name"]
        user.last_name = request.POST["last_name"]
        user.save()

        profile = Profile(user=user)
        profile.save()

        ctx = {
            "message":"User created with successfully"
        }
        return render(request,"users/register.html",ctx)

    return render(request,"users/register.html")
