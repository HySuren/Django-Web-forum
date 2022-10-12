from django.shortcuts import render, HttpResponse
from rest_framework import generics
from .Selerizers import Serializers
from .models import User


def post_db(*args, **kwargs):
    pass


class urls_all:
    def search(request):
        data = requests.get(
            f"{User}")
        return data.json()['puuid']

    def login(request):
        return render(request, 'login.html')

    def register(request):
        return render(request, 'Register.html')

    def postuser(request):
        user_id = ''
        form = ''
        if request.method == "POST":
            form = User(request.POST)
            print('form is coming')
            # form.cleaned_data["name"]
            return HttpResponse('<h2> form submitted.</h2>')  # just for testing purpose you can remove it.
        else:
            form = User()
            user_id = search(request)
        return render(request, "Register.html", {
            'form': form,  # Reference to form
            'userid': user_id,
            # 'mmr':NA,
        })

    def load_info(request):
        return HttpResponse(f"<h2>Login: {User.login}    Password: {User.password}</h2>")
        login = request.POST("login", User.login)
        password = request.POST("password",User.password)
        return HttpResponse(f"<h2>Login: {login}    Password: {password}</h2>")
