""" User's urls """

""" Django """
from django.urls import path

"""Local views"""
from users import views

urlpatterns = [

    path(
        route='profile/<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),

    path(
        route='logout/',
        view=views.logout_view,
        name='logout'
    ),

    path(
        route='register/',
        view=views.RegisterFormView.as_view(),
        name='register'
    ),

    path(
        route='login/',
        view=views.login_view,
        name='login'
    ),
    path(route='me/profile/',
        view=views.update_profile,
        name='update_profile'
    ),
]
