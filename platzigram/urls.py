""" platzigram URL'S Module"""

"""platzigram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Django
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from django.conf import settings

#Project 'Platzigram'
from platzigram import views as local_views
from posts import views as posts_views
from users import views as users_views

urlpatterns = [
    #Django
    path('admin/', admin.site.urls,name='admin'),
    # Posts
    path('',posts_views.list_posts,name='feed'),
    path('posts/new/',posts_views.create_post,name='create_post'),
    # Users
    path('users/logout/',users_views.logout_view,name='logout'),
    path('users/register/',users_views.register_view,name='register'),
    path('users/login',users_views.login_view,name='login'),
    path('users/se/profile/',users_views.update_profile,name='update_profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
