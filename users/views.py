"""Views Users."""

# Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Local
from users.models import Profile
from users.forms import ProfileForm, SignupForm
# Create your views here.


@login_required
def update_profile(request):
    """ Update a user's profile view. """
    profile = request.user.profile

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            profile.picture = data["picture"]
            profile.website = data["website"]
            profile.phone_number = data["phone_number"]
            profile.biography = data["biography"]
            profile.save()
            return redirect('feed')
    else:
        form = ProfileForm()


    ctx = {
        "user"   : request.user,
        "profile": profile,
        "form"   : form,
    }
    return render(
            request       = request,
            template_name ="users/update_profile.html",
            context       = ctx,
        )

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
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            ctx = {
                "form":form,
                "message":"User created with successfull",
            }
            return render(request,"users/register.html",ctx)
        else:
            print(form.errors.as_data())

    else:
        form = SignupForm()
    ctx = {
        "form":form
    }
    return render(request,"users/register.html",ctx)
