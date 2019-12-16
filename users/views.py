"""Views Users."""

""" Django imports. """
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, UpdateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

""" Local imports """
from users.models import Profile
from posts.models import Post
from users.forms import ProfileForm, SignupForm, LoginForm
# Create your views here.

class UserDetailView(DetailView):
    """ User detail view. """

    template_name = 'users/details.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self,**kwargs):
        """Add user's posts to context"""
        context = super().get_context_data(**kwargs)

        user = self.get_object()
        context['posts'] = Post.objects.filter(profile_id=user.profile).order_by('-created')
        context['posts_count'] = len(context['posts'])
        return context

class RegisterFormView(FormView):
    success_url = reverse_lazy("users:login")
    form_class = SignupForm
    template_name = "users/register.html"

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)


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

            url = reverse_lazy('users:detail',kwargs={'username':request.user.username})
            print(url)
            return redirect(url)
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
    error = ""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            data = form.cleaned_data

            username = data["username"]
            password = data["password"]
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                return redirect('posts:feed')

            else:
                error = "User or password do not match"

        # Else redirect to the login
    else:
        form = LoginForm()

    ctx = {
        "form" : form,
        "error": error,
    }
    return render(request,"users/login.html",ctx)


@login_required()
def logout_view(request):
    """ Logout View. """
    logout(request)
    return redirect('users:login')
