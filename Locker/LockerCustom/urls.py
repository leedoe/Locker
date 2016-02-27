from django.conf.urls import include, url
from django.contrib import admin
from . import views
from LockerCustom.forms import LoginForm

urlpatterns = [
    # 로그인 url
    url(r'^$',
        'django.contrib.auth.views.login',
        name='login',
        kwargs={'template_name': 'LockerCustom/LoginPage.html', 'authentication_form': LoginForm}),
    # 로그아웃 url
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout', kwargs={'next_page': '/'}),
    # 사용자 정보 url
    url(r'^Profile/$', views.profile, name='profile'),
    # 사물함 선택
    url(r'^LockerChoice/$', views.locker_choice, name='locker_choice'),
]
