from django.db import transaction
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.template import loader, Context
from django.views.generic import View
from django.http import HttpResponse
from .forms import UserInfoForm
from .models import UserInfo, Locker, LockerDetail
import logging


def login_page(request):
    # 로그인 페이지 뷰 /
    form = UserInfoForm()
    return render(request, 'LockerCustom/LoginPage.html', {'form': form})


def profile(request):
    # 로그인 후 사용자 정보 및 사물함 신청 버튼 뷰, /Profile
    user = None
    fee = None
    if request.user.is_authenticated():
        user = request.user
        if user.fee_check is 0:
            fee = '회비 미납'
        else:
            fee = '회비 납부'
    else:
        return redirect('/')

    try:
        user_locker = LockerDetail.objects.get(user_id=user.id)
    except:
        user_locker = None
    return render(request, 'LockerCustom/Profile.html', {'user': user, 'fee': fee, 'user_locker': user_locker})


"""
def locker_detail(request):
    user = None
    if request.user.is_authenticated():
        user = request.user
    else:
        return redirect('/')

    locker = Locker.objects.filter(manager=user.department_id).order_by('section').order_by('floor')
    lockerdetail = list()

    for index, i in enumerate(locker):
        lockerdetail.append([])
        detail_obj = LockerDetail.objects.filter(locker_number_id=i.id)
        for j in detail_obj:
            lockerdetail[index].append(j)

    return render(request, 'LockerCustom/lockerdetail.html', {'locker': locker, 'lockerdetail': lockerdetail})
"""


def locker_choice(request):
    user = None
    if request.user.is_authenticated():
        user = request.user
    else:
        return redirect('/')

    if request.is_ajax():
        if request.POST:
            print(request.POST)
            try:
                detail_id = request.POST['locker']
            except:
                detail_id = None
            locker_id = request.POST['locker']
            locker = Locker.objects.get(id=int(locker_id))
            lockerDetail = LockerDetail.objects.filter(locker_number=locker.id).order_by('locker_detail_number')
            csrf_token = request.POST['csrfmiddlewaretoken']

            tpl = loader.get_template('LockerCustom/detail.html')
            ctx = Context({'locker': locker, 'detail': lockerDetail, 'csrf_token': csrf_token})

            return HttpResponse(tpl.render(ctx))

    locker = Locker.objects.filter(manager=user.department_id).order_by('section').order_by('floor')
    return render(request, 'LockerCustom/lockerChoice.html', {'locker': locker})


def locker_content(request, locker_id=None):
    user = None
    test = None
    locker = Locker.objects.get(id=int(locker_id))
    lockerDetail = LockerDetail.objects.filter(locker_number=locker.id).order_by('locker_detail_number')

    if request.user.is_authenticated():
        user = request.user
    else:
        return redirect('/')

    with transaction.atomic():
        if request.POST:
            detail_id = request.POST['detail_id']
            lock_id = request.POST['locker']

            detail = LockerDetail.objects.get(id=detail_id)
            user_locker = None
            try:
                user_locker = LockerDetail.objects.get(user_id=user.id)
            except:
                user_locker = None

            if user_locker is not None:
                messages.error(request, '이미 사물함을 예약하셨습니다')
                return render(request, 'LockerCustom/detail.html', {'locker': locker, 'detail': lockerDetail})
            elif detail.check == 0:
                messages.error(request, '해당 사물함은 이미 예약 되었습니다.');
                return render(request, 'LockerCustom/detail.html', {'locker': locker, 'detail': lockerDetail})
            detail.user_id_id = user.id
            detail.check = 0
            detail.save()

    return render(request, 'LockerCustom/detail.html', {'locker': locker, 'detail': lockerDetail})


def locker_detail_ajax(request, locker_id=None):
    locker = Locker.objects.get(id=int(locker_id))
    lockerDetail = LockerDetail.objects.filter(locker_number=locker.id).order_by('locker_detail_number')
    tpl = loader.get_template('LockerCustom/detail.html')
    ctx = Context({'locker': locker, 'detail': lockerDetail})

    if request.user.is_authenticated():
        user = request.user
    else:
        return redirect('/')

    with transaction.atomic():
        if request.POST:
            detail_id = request.POST['detail_id']
            lock_id = request.POST['locker']

            detail = LockerDetail.objects.get(id=detail_id)
            user_locker = None
            try:
                user_locker = LockerDetail.objects.get(user_id=user.id)
            except:
                user_locker = None

            if user_locker is not None:
                messages.error(request, '이미 사물함을 예약하셨습니다')
                return render(request, 'LockerCustom/detail.html', {'locker': locker, 'detail': lockerDetail})
            elif detail.check == 0:
                messages.error(request, '해당 사물함은 이미 예약 되었습니다.');
                return render(request, 'LockerCustom/detail.html', {'locker': locker, 'detail': lockerDetail})
            detail.user_id_id = user.id
            detail.check = 0
            detail.save()
    # return HttpResponse(tpl.render(ctx))
    return render(request, 'LockerCustom/detail.html', {'locker': locker, 'detail': lockerDetail})
