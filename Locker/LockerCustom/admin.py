from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AdminPasswordChangeForm
from django.http import request

from .models import *
from openpyxl import load_workbook


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
    password = ReadOnlyPasswordHashField(label= ("Password"),
        help_text= ("Raw passwords are not stored, so there is no way to see "
                    "this user's password, but you can change the password "
                    "using <a href=\"password/\">this form</a>."))

    class Meta:
        model = UserInfo
        fields = ['username', 'first_name', 'fee_check', 'department']


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'first_name', 'department', 'fee_check')
    list_filter = ('department', 'fee_check', )
    actions = ['fee_change']
    search_fields = ['username', 'first_name']
    """form = UserCreationForm
    change_form = UserChangeForm"""

    def fee_change(modeladmin, request, queryset):
        queryset.update(fee_check=1)
    fee_change.short_description = "선택된 회원을 '회비 납부'로 변경"

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
        fields = ("floor", "section", "rNum", "cNum", "start_number", "building", "manager", "map")


class LockerAdmin(admin.ModelAdmin):
    form = LockerForm
    list_display = ('__str__', 'manager')

    # Locker를 생성할 때 LockerDetail을 생성
    def save_model(self, request, obj, form, change):
        obj.save()
        """
        for i in range(1, obj.rNum + 1):
            for j in range(1, obj.cNum + 1):
                detail_number = (i - 1) + obj.rNum * (j - 1) + obj.start_number
                LockerDetail(locker_number=obj, locker_detail_number=detail_number, row=i, column=j, check=1).save()
        """
        for j in range(1, obj.cNum + 1):
            for i in range(1, obj.rNum + 1):
                detail_number = (i - 1) + obj.rNum * (j - 1) + obj.start_number
                LockerDetail(locker_number=obj, locker_detail_number=detail_number, row=i, column=j, check=1).save()

    # Locker를 지울 때 Locker와 연결된 LockerDetail을 모두 삭제
    def delete_model(self, request, obj):
        LockerDetail.objects.filter(locker_number=obj).delete()
        obj.delete()


class Register_Time(admin.ModelAdmin):
    list_display = ('department', 'start_time', 'end_time')

    class Meta:
        model = RegisterTime


class LockerDetail_adminClass(admin.ModelAdmin):
    list_display = ('__str__', 'check', 'user_id')
    list_filter = ('locker_number', )

    class Meta:
        model = LockerDetail


class ExcelPath_adminClass(admin.ModelAdmin):
    class Meta:
        model = ExcelPath

    def save_model(self, request, obj, form, change):
        obj.save()
        path = obj.excelpath

        #엑셀파일을 DB에 저장
        wb = load_workbook(filename=path)
        sheet_list = wb.get_sheet_names()
        sheet = wb.get_sheet_by_name(sheet_list[0])

        for row in sheet:
            if str(row[1].value).isdigit():
                USERNAME = str(row[1].value)
                NAME = str(row[2].value)
                DEPARTMENT = obj.department
                if str(row[4].value) == '완납':
                    FEE_CHECK = 1
                else:
                    FEE_CHECK = 0

                if str(row[3].value).replace("-", "")[-8:] == "":
                    PASSWORD = "IT"
                else:
                    PASSWORD = str(row[3].value).replace("-", "")[-8:]

                try:
                    user = UserInfo.objects.get(username=USERNAME)
                    user.fee_check = FEE_CHECK
                    user.save()
                except:
                    user = UserInfo(username=str(USERNAME), first_name=NAME, fee_check=0, department=DEPARTMENT)
                    user.set_password(PASSWORD)
                    user.save()


admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(Building)
admin.site.register(Department)
admin.site.register(Locker, LockerAdmin)
admin.site.register(LockerDetail, LockerDetail_adminClass)
admin.site.register(RegisterTime, Register_Time)
admin.site.register(ExcelPath, ExcelPath_adminClass)
