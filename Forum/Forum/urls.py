from django.contrib import admin
from django.urls import path, include
from Forum_app.views import ClientCreate,urls_all
from Forum_app.Selerizers import Serializers


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Forum_app.urls')),
]
