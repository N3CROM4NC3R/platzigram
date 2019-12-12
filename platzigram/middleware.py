""" Platzigram middleware catalog. """

# Django
from django.shortcuts import redirect
from django.urls import reverse



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
                if request.path not in [reverse('update_profile'),reverse('logout')]:
                    return redirect("update_profile")

        response = self.get_response(request)
        return response

class ActiveUserMiddleware:
    """Active user Middleware

    Ensure if have a active user redirect to the feed
    """

    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):

        if not request.user.is_anonymous:
            if request.path == reverse('login') or request.path == reverse('register'):
             return redirect('feed')

        response = self.get_response(request)
        return response
