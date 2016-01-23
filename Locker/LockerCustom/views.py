from django.shortcuts import render, redirect
from .forms import UserInfoForm
from .models import UserInfo


def login_page(request):
    if request.method == "POST":
        form = UserInfoForm(request.POST)

    form = UserInfoForm()
    return render(request, 'LockerCustom/LoginPage.html', {'form': form})
