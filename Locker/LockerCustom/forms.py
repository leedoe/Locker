from django import forms
from django.contrib.auth.models import User   # fill in custom user info then save it
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserInfo
from django.contrib.auth import get_user_model


class UserInfoForm(AuthenticationForm):
    class Meta:
        model = UserInfo
        fields = ('username', 'password',)
