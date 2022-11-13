from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import User
import random

array = {
    'login': '',
    'password': '',
    'keys_id': 0,
    'is_active': False,
}


def generate_keys():
    keys = random.choice(range(235346, 9999999))
    return keys


def user_save_registor(array: dict, login: str, password: str, keys_id: int, active: bool):
    array['login'] = login
    array['password'] = password
    array['keys_id'] = keys_id
    array['is_active'] = active
    return array


def user_save_login(array: dict, login: str, password: str, active: bool):
    array['login'] = login
    array['password'] = password
    array['is_active'] = active
    return array


def user_ofline(array: dict, active: bool):
    array['is_active'] = active
    return array


class urls_all:

    def home(request):
        if array['is_active'] == True:
            return render(request, 'home_users.html')
        return render(request, 'home.html')

    def login(request):
        return render(request, 'login.html')

    def register(request):
        return render(request, 'Register.html')

    def user_cabinet(request):
        activate = True
        login_filter = User.objects.filter(is_active=True)
        if activate == login_filter.exists():
            login = array.get('login')
            info = User.objects.filter(login=login)
            return render(request, 'lk_Cabinet.html', locals())
        else:
            return HttpResponse('<h1>Технические проблемы</h1>')

    def user_register(request):
        """user_register() проверяет по бд, есть ли юзер
        с таким логином , если нет то добовляет в базу
        и переноправляет в ЛК
        """
        login = request.POST.get('login')
        password = request.POST.get('password')
        login_filter = User.objects.filter(login=login)
        if login_filter.exists():
            return HttpResponse(
                "<h1>Пользователь с данным логином уже есть!</h1> \n <a href='register'>Вернутся к регистрации<a>")
        if len(password) < 8:
            return HttpResponse(
                "<h1>Пароль должен содержать не мение 8 символов!</h1> \n <a href='register'>Вернутся к регистрации<a>")
        else:
            user = User()
            user.login = login
            user.password = password
            user.keys_id = generate_keys()
            user_save_registor(array, login, password, user.keys_id, False)
            user.save()
            return HttpResponseRedirect('login')

    def user_login(request):
        """user_login() , проверяет логин и пороль по бд,
        и если юзер зареган то redirect на ЛК
        """
        active = True
        login = request.POST.get('login')  # Получаем логин
        password = request.POST.get('password')  # Получаем пароль
        login_filter = User.objects.filter(login=login, password=password)
        if login_filter.exists():
            user_save_login(array, login, password, True)
            User.objects.filter(login=login).update(is_active=True)
            info = User.objects.filter(login=login)
            return render(request, 'lk_Cabinet.html', locals())
        else:
            return HttpResponse(
                "<h1>Не верный логин или пароль!</h1> \n <a href='login'>Попробовать ещё раз<a>")

    def is_online(request):
        user_ofline(array, False)
        return render(request, 'home.html')
