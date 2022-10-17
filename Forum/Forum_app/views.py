from django.shortcuts import render, HttpResponse
from rest_framework import generics
from .Selerizers import Serializers
from .models import User


class urls_all:

    def home(request):
        return render(request, 'home.html')

    def login(request):
        return render(request, 'login.html')

    def register(request):
        return render(request, 'Register.html')

    def user_cabinet(request):
        return render(request, 'lk_Cabinet.html')


class ClientCreate(generics.CreateAPIView):
    serializer_class = Serializers.UserCreate


class UserView(generics.ListAPIView):
    serializer_class = Serializers.ValidatorUser
    queryset = User.objects.all()
