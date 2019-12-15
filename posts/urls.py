""" Post Urls. """

""" Django """
from django.urls import path

"""Local views"""
from posts import views


urlpatterns = [
    path(
        route='',
        view=views.ListPostsView.as_view(),
        name='feed'
    ),
    path(
        route='new/',
        view=views.create_post,
        name='create_post'
    ),
]