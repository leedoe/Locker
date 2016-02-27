from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=8,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'ID',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
            }
        )
    )