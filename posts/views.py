""" Posts views """
# Django
from django.shortcuts import render,redirect
from django.db import models
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
#Local
from users.models import Profile
from posts.models import Post
from posts.forms import PostForm

# Utilities
from datetime import datetime
# Create your views here.

class ListPostsView(LoginRequiredMixin,ListView):
    model = Post
    template_name = "posts/feed.html"
    context_object_name = "posts"
    paginate_by = 2

class DetailPostView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = "posts/details.html"
    context_object_name = "post"
    slug_url_kwarg = "post"
    slug_field = "id"





@login_required()
def create_post(request):
    """Create post

        Create a new post for the user
    """
    profile = request.user.profile

    if request.method == 'POST':

        form = PostForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()

            return redirect('posts:feed')
    else:
        form = PostForm()

    ctx = {
        "user": request.user,
        "profile": profile,
        "form" : form,
    }
    return render(request,'posts/create_post.html',ctx)
