""" Posts views """
# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.db import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
#Local
from users.models import Profile
from posts.models import Post
from posts.forms import PostForm

# Utilities
from datetime import datetime
# Create your views here.

class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = "posts/feed.html"
    context_object_name = "posts"
    ordering = ('-created')
    paginate_by = 30

class PostDetailView(LoginRequiredMixin,DetailView):
    queryset = Post.objects.all()
    template_name = "posts/details.html"
    context_object_name = "post"

class PostCreateView(LoginRequiredMixin,CreateView):
    template_name = "posts/create_post.html"
    form_class = PostForm
    success_url = reverse_lazy("posts:feed")

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)

        context["profile"] = self.request.user.profile

        return context


@login_required
def PostLikeToggle(request,post_id):

    post = Post.objects.filter(id=post_id)

    if post:
        post = Post.objects.get(id=post_id)
        profile = Profile.objects.get(id=request.user.profile.id)
        print(post.likes.count())
        if not profile in post.likes.all():
            post.likes.add(profile)
        else:
            post.likes.remove(profile)
        post.save()
    return redirect("posts:feed")
