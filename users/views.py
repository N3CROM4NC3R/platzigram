"""Views Users."""

""" Django imports. """
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, UpdateView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

""" Local imports """
from users.models import Profile
from posts.models import Post
from users.forms import ProfileForm, SignupForm, LoginForm
# Create your views here.

class UserDetailView(LoginRequiredMixin,DetailView):
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

class ProfileUpdateView(LoginRequiredMixin,UpdateView):
    model = Profile
    template_name = "users/update_profile.html"
    fields = ['website','phone_number','biography','picture']
    success_url = reverse_lazy("posts:feed")
    def get_object(self):
        return self.request.user.profile

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)

        context["user"] = self.request.user
        context["profile"] = self.request.user.profile

        return context

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)

class UserLoginView(LoginView):
    model = User
    template_name = "users/login.html"
    redirect_authenticated_user = reverse_lazy("posts:feed")
    form_class = LoginForm



class UserLogoutView(LogoutView):

    template_name = "users/logot.html"


@login_required()
def logout_view(request):
    """ Logout View. """
    logout(request)
    return redirect('users:login')
