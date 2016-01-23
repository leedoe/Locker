from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.http import request

from .models import *


# Register your models here.
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="비밀번호",
                                widget=forms.PasswordInput)

    class Meta:
        model = UserInfo
        fields = ("username", "fee_check", "department")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserInfoAdmin(admin.ModelAdmin):
    form = UserCreationForm


admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(Building)
admin.site.register(Department)
admin.site.register(Locker)
admin.site.register(LockerDetail)
