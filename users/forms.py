""" Users forms classes. """
""" Django """
# Form
from django import forms
from django.contrib.auth import authenticate
# Contrib
from django.contrib.auth.models import User
""" Locals """
# Models
from users.models import Profile

class  LoginForm(forms.Form):
    username = forms.CharField(
                                label=False,
                                max_length=100,
                                widget=forms.TextInput(
                                    attrs={
                                        "class":"form-control mb-3",
                                        "required":True,
                                        "placeholder":"Username",
                                    }))
    password = forms.CharField(
                                label=False,
                                min_length=8,
                                max_length=70,
                                widget=forms.PasswordInput(
                                    attrs={
                                        "class":"form-control mb-3",
                                        "required":True,
                                        "placeholder":"Password",
                                    }
                                )
                            )



class SignupForm(forms.Form):
    """ Register/Sign-up Form. """

    username = forms.CharField(
                                label=False,
                                max_length=100,
                                widget=forms.TextInput(
                                    attrs={
                                        "class":"form-control mb-3",
                                        "required":True,
                                        "placeholder":"Username",
                                    }))


    first_name = forms.CharField(
                                label=False,
                                min_length=2,
                                max_length=20,
                                widget=forms.TextInput(
                                    attrs={
                                        "class":"form-control mb-3",
                                        "required":True,
                                        "placeholder":"First name",
                                    }))
    last_name = forms.CharField(
                                label=False,
                                min_length=2,
                                max_length=20,
                                widget=forms.TextInput(
                                    attrs={
                                        "class":"form-control mb-3",
                                        "required":True,
                                        "placeholder":"Last name",
                                    }))

    email = forms.EmailField(
                            label=False,
                            min_length=6,
                            max_length=70,
                            widget=forms.EmailInput(
                                                attrs={
                                                    "class":"form-control mb-3",
                                                    "required":True,
                                                    "placeholder":"Email",
                                                }))

    password = forms.CharField(
                                label=False,
                                min_length=8,
                                max_length=70,
                                widget=forms.PasswordInput(
                                    attrs={
                                        "class":"form-control mb-3",
                                        "required":True,
                                        "placeholder":"Password",
                                    }
                            ))
    password_confirmation = forms.CharField(
                                            label=False,
                                            min_length=8,
                                            max_length=70,
                                            widget=forms.PasswordInput(
                                                attrs={
                                                "class":"form-control mb-3",
                                                "required":True,
                                                "placeholder":"Password confirmation",
                                                }
                                            ))

    def clean_username(self):

        username = self.cleaned_data["username"]
        username_taken = User.objects.filter(username=username).exists()

        if username_taken:
            this.add_error('username','Username is already in use.')
            raise forms.ValidationError('Username is already in use.')

        return username

    def clean_email(self):

        email = self.cleaned_data["email"]
        email_taken = User.objects.filter(email=email).exists()

        if email_taken:
            self.add_error("email",'Email is already in use')
            raise forms.ValidationError('Email is already in use')

        return email
    def clean(self):
        data = super().clean()
        password = data["password"]
        password_confirmation = data["password_confirmation"]
        if password != password_confirmation:
            self.add_error("password","Password do not match")
            raise forms.ValidationError("Password do not match")

        return data

    def save(self):
        """Create a new User and profile """
        data = self.cleaned_data
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()


class ProfileForm(forms.Form):
    """ Update Profile Form."""
    website = forms.URLField(
                            max_length=200,
                            required=True,
                            widget=forms.URLInput(
                                attrs={
                                        "class":"form-control",
                                        "required":True,
                                        "placeholder":"Website",
                                        "max_length":"200",
                                }
                            ))
    Biography = forms.CharField(
                                max_length=500,
                                required=True,
                                widget=forms.TextInput(attrs={
                                    "class":"form-control",
                                    "placeholder":"Biography",
                                    "max_length":"500",
                                    "required":True,
                                }))

    phone_number = forms.CharField(
                                    max_length=20,
                                    required=False,
                                    widget=forms.TextInput(attrs={
                                        "class":"form-control",
                                        "placeholder":"Phone Number",
                                        "max_length":"20",
                                        "required":True,
                                    }))

    picture = forms.ImageField(widget=forms.FileInput(
                                                    attrs={
                                                        "class":"form-control"
                                                    }
    ))
