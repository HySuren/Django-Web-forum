from Forum_app.views import urls_all
from django.urls import re_path


app_name = 'Forum_app'
urlpatterns = [
    re_path(r'home', urls_all.home),
    re_path(r'register', urls_all.register),
    re_path(r'create', urls_all.user_register),
    re_path(r'validation', urls_all.user_login),
    re_path(r'user_cabinet', urls_all.user_cabinet),
    re_path(r'login', urls_all.login),
    re_path(r'is_online', urls_all.is_online),
    re_path(r'', urls_all.home)
]
