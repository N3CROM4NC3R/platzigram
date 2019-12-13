"""Posts forms based in classes. """
# Django
from django.forms import ModelForm

# Local
from posts.models import Post

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['profile','title','photo',]
