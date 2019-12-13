"""Views Users."""

# Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Local
from users.models import Profile
from users.forms import ProfileForm
# Create your views here.


@login_required
def update_profile(request):
    """ Update a user's profile view. """
    profile = request.user.profile

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile.picture = form.cleaned_data["picture"]
            profile.website = form.cleaned_data["website"]
            profile.phone_number = form.cleaned_data["phone_number"]
            profile.biography = form.cleaned_data["biography"]
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
