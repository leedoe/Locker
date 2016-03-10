from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib import messages
from django.template import loader, Context
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

from .forms import LoginForm, LockerDetailForm
from .models import Locker, LockerDetail, RegisterTime

import time


def login_page(request):
    # 로그인 페이지 뷰 /
    form = LoginForm()
    return render(request, 'LockerCustom/LoginPage.html', {'form': form})


@login_required
def profile(request):
    # 로그인 후 사용자 정보 및 사물함 신청 버튼 뷰, /Profile
    user = None
    fee = None
    RT = RegisterTime.objects.order_by('department')
    if request.POST:
        user_id = request.POST['user_id']
        locker_detail = LockerDetail.objects.get(user_id=user_id)
        locker_detail.user_id = None
        locker_detail.check = 1
        locker_detail.save()

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
    return render(request, 'LockerCustom/Profile.html', {'user': user, 'fee': fee, 'user_locker': user_locker, 'time': RT})


@login_required
def locker_choice(request):
    user = None
    if request.user.is_authenticated():
        user = request.user
        RT = RegisterTime.objects.get(department=user.department)

        if not (timezone.now() >= RT.start_time and timezone.now() <= RT.end_time):
            messages.error(request, "예약 가능한 시간이 아닙니다")
            return redirect('profile')

        if user.fee_check is 0:
            fee = '회비 미납'
        else:
            fee = '회비 납부'
    else:
        return redirect('/')

    locker = Locker.objects.filter(manager=user.department_id).order_by('section').order_by('floor')

    #ajax 사물함 보여주기
    if request.is_ajax():
        if request.POST:
            locker_id = request.POST['locker']
            locker = Locker.objects.get(id=int(locker_id))
            lockerDetail = LockerDetail.objects.filter(locker_number=locker.id).order_by('locker_detail_number')
            csrf_token = request.POST['csrfmiddlewaretoken']
            ldf = LockerDetailForm()
            ldf.get_locker(locker, lockerDetail)

            tpl = loader.get_template('LockerCustom/detail.html')
            ctx = Context({'locker': locker, 'detail': lockerDetail, 'ldf': ldf, 'csrf_token': csrf_token})

            return HttpResponse(tpl.render(ctx))
    else:
        #사물함 신청 transaction
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
                    return render(request, 'LockerCustom/lockerChoice.html', {'locker': locker})
                elif detail.check == 0:
                    messages.error(request, '해당 사물함은 이미 예약 되었습니다.');
                    return render(request, 'LockerCustom/lockerChoice.html', {'locker': locker})
                detail.user_id_id = user.id
                detail.check = 0
                detail.save()
                messages.info(request, '정상적으로 예약 되었습니다')
                return render(request, 'LockerCustom/lockerChoice.html', {'locker': locker})

    return render(request, 'LockerCustom/lockerChoice.html', {'locker': locker})