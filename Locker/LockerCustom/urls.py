from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # 로그인 url
    url(r'^$', 'django.contrib.auth.views.login', name='login'),
    # 로그아웃 url
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout', kwargs={'next_page': '/'}),
    # 사용자 정보 url
    url(r'^Profile/$', views.profile, name='profile'),
    # 사물함 선택
    url(r'^LockerChoice/$', views.locker_choice, name='locker_choice'),
    # 사물함 내용
    url(r'^LockerDetail/(?P<locker_id>\d+)/$', views.locker_content, name='locker_contents'),
    url(r'^LockerDetail/ajax/(?P<locker_id>\d+)/$', views.locker_detail_ajax, name='ajax_test')

    #url(r'LockerDetail/$', views.locker_detail, name='locker_detail')
]
