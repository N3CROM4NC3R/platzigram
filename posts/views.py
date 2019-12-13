""" Posts views """
# Django
from django.shortcuts import render,redirect
from django.db import models
from django.contrib.auth.decorators import login_required
#Local
from users.models import Profile
from posts.models import Post
from posts.forms import PostForm

# Utilities
from datetime import datetime
# Create your views here.

@login_required()
def list_posts(request):
    """list Posts
    Show all Platzigram's posts in feed
    """
    posts = Post.objects.all()
    user = request.user
    profile = user.profile
    ctx = {
        "user"    : user,
        "profile" : profile,
        "posts" : posts
    }
    return render(request,'posts/feed.html',ctx)

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

            return redirect('feed')
    else:
        form = PostForm()

    ctx = {
        "user": request.user,
        "profile": profile,
        "form" : form,
    }
    return render(request,'posts/create_post.html',ctx)
