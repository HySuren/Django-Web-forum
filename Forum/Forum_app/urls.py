from Forum_app.views import UserView,ClientCreate, urls_all
from Forum_app.Selerizers import Serializers
from django.urls import path,re_path

app_name = 'Forum_app'
urlpatterns = [
    re_path(r'home/$', urls_all.home),
    re_path(r'register/$', urls_all.register),
    re_path(r'create_user/$', ClientCreate.as_view()),
    re_path(r'info/$', UserView.as_view()),
    re_path(r'user_cabinet/$', urls_all.user_cabinet),
    re_path(r'login/$', urls_all.login)
]
