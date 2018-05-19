from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User


class Edit(UserChangeForm):
    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "password"
        ]


class changePassword(UserChangeForm):
    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "password"
     ]