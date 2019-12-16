""" Platzigram middleware catalog. """

""" Django Imports """
from django.shortcuts import redirect
from django.urls import reverse_lazy

""" Local Imports. """

#Models
from users.models import Profile

class ProfileCreateMiddleware:
    """Profile Create MIDDLEWARE

        If the profile of the user active is eliminated
        this middleware will create her
    """

    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        if not request.user.is_anonymous:
            if not hasattr(request.user,'profile'):
                profile = Profile(user=request.user)
                profile.save()
                redirect("users:update_profile")

        response = self.get_response(request)

        return response
class ProfileCompletionMiddleware:
    """Profile completion middleware

    Ensure every user that is interesting in
    interact with the plataform had the profile complete

    """
    def __init__(self,get_response):
        """Middleware Initialization"""
        self.get_response = get_response

    def __call__(self,request):
        """ Code to be executed for each request before the view is called """

        if not request.user.is_anonymous:
            profile = request.user.profile

            if not profile.picture or not profile.biography:
                if request.path not in [reverse_lazy('users:update_profile'),reverse_lazy('users:logout')]:
                    return redirect("users:update_profile")

        response = self.get_response(request)
        return response




class ActiveUserMiddleware:
    """Active user Middleware

    Makes sure that an active user upon register
    or login is redirected to feed
    """

    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):

        if not request.user.is_anonymous:
            if request.path == reverse_lazy('users:login') or request.path == reverse_lazy('users:register'):
             return redirect('posts:feed')

        response = self.get_response(request)
        return response
