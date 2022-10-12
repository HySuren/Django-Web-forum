from django.contrib import admin
from django.urls import path, include
from Forum_app.views import urls_all
from Forum_app.Selerizers import Serializers


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', urls_all.login),
    path('register/postuser/', urls_all.postuser),
    path('info',urls_all.load_info),
    path('register/',urls_all.register)
]
