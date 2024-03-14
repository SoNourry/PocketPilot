# coding=utf-8
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import django.forms as forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text="")

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )
