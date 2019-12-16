""" Post Urls. """

""" Django """
from django.urls import path

"""Local views"""
from posts import views


urlpatterns = [
    path(
        route="detail-post/<slug:pk>",
        view=views.PostDetailView.as_view(),
        name="detail"
    ),
    path(
        route='',
        view=views.PostListView.as_view(),
        name='feed'
    ),
    path(
        route='new/',
        view=views.PostCreateView.as_view(),
        name='create_post'
    ),
]
