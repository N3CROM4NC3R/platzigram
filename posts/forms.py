"""Posts forms based in classes. """
# Django
from django import forms

# Local
from posts.models import Post

class PostForm(forms.ModelForm):



    class Meta:
        model = Post
        fields = ['profile','title','photo',]
