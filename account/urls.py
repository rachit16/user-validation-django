from django.contrib import admin
from django.conf import settings
from django.urls import path,re_path,include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth import urls


app_name='account'

urlpatterns = [
    re_path(r'^$' , views.login),
    re_path(r'^register/$', views.register, name='register'),
    #re_path(r'^password-change-done/$',auth_views.password_change_done,name='password_change_done'),
    re_path(r'^password-change/$',views.password_change,name='password_change'),
    re_path(r'^login/$', views.login, name='account_login'),
    re_path(r'^logout/$', views.logout, name='account_logout'),
    re_path(r'^admin_page/$', views.admin_page, name='admin_page'),
    re_path(r'^sc_registration/$', views.sc_registration, name='sc_registration'),
]
