from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.http import request

from .models import *


# Register your models here.
# 사용자 정보 폼
class UserCreationForm(forms.ModelForm):
    # password1 = forms.CharField(label="비밀번호", widget=forms.PasswordInput)

    class Meta:
        model = UserInfo
        fields = ["username", "password", "first_name", "fee_check", "department"]

    # 비밀번호 암호화
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['username', 'first_name', 'fee_check', 'department']


class UserInfoAdmin(admin.ModelAdmin):
    """form = UserCreationForm
    change_form = UserChangeForm"""
    # 유저 생성은 비밀번호 폼이 나오고 수정은 비밀번호가 안나오게 변경
    # 유저 수정 시 비밀번호가 나올경우 해싱된 비밀번호가 또 다시 해싱되 값이 자꾸 변경됨
    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            return UserCreationForm
        else:
            return UserChangeForm


# 사물함 생성 시 세부 정보 생성
class LockerForm(forms.ModelForm):
    class Meta:
        model = Locker
        fields = ("floor", "section", "rNum", "cNum", "building", "manager")


class LockerAdmin(admin.ModelAdmin):
    form = LockerForm

    # Locker를 생성할 때 LockerDetail을 생성
    def save_model(self, request, obj, form, change):
        obj.save()

        for i in range(1, obj.rNum + 1):
            for j in range(1, obj.cNum + 1):
                detail_number = (i-1) * obj.cNum + j
                LockerDetail(locker_number=obj, locker_detail_number=detail_number,row=i, column=j, check=1).save()

    # Locker를 지울 때 Locker와 연결된 LockerDetail을 모두 삭제
    def delete_model(self, request, obj):
        LockerDetail.objects.filter(locker_number=obj).delete()
        obj.delete()


admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(Building)
admin.site.register(Department)
admin.site.register(Locker, LockerAdmin)
admin.site.register(LockerDetail)
