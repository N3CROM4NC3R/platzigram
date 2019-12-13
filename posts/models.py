"""Posts models."""

#Django
from django.db import models
from django.contrib.auth.models import User

#Local
from users.models import Profile

class Post(models.Model):
    """ Post model. """

    profile = models.ForeignKey(
        'users.Profile',
        on_delete = models.CASCADE,
    )

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """ Return title and username. """
        return "{title} by @{username}".format(
            title=self.title,
            username=self.profile.user.username,
        )
    def username(self):
        return self.profile.user
