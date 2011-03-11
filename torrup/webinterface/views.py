# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

from torrup.webinterface.models import *

# Вывод формы регистрации
def registration_form(request):
    return render_to_response('registration_form.html', {'show_form':True, 'message':''})
    
# Обработка заполненной формы и вывод поздравления о регистрации
@csrf_exempt
def registration(request):
    get_login = request.POST.get('login','')
    get_password1 = request.POST.get('password1','')
    get_password2 = request.POST.get('password2','')
    
    profile = Profile.objects.filter(username=get_login)
    # Проверка, существует ли пользователь с таким именем.
    if profile:
        return render_to_response('registration_form.html', {'last_login':get_login, 
                                                             'last_password1':get_password1, 
                                                             'last_password2':get_password2,
                                                             'show_form':True, 
                                                             'message':'Пользователь с таким именем уже существует.'})
    # Проверка, являются ли введенные пароли одинаковыми
    elif get_password1 == get_password2 and get_password1 != '' and get_password2 != '':
        profile = Profile(username=get_login)
        profile.set_password(get_password1)
        profile.save()

        return render_to_response('registration_form.html', {'show_form':False, 
                                                             'message':'Поздравляем, вы успешно зарегистрировались. Войдите в систему.'})
    # Если пароли не одинаковые
    else:
        return render_to_response('registration_form.html', {'last_login':get_login, 
                                                             'last_password1':get_password1, 
                                                             'last_password2':get_password2,
                                                             'show_form':True, 
                                                             'message':'Пароли не совпадают.'})

# Форма аутентификации пользователя
@csrf_exempt
def authentication_form(request):
    if 'login' in request.POST and 'password' in request.POST:
        profile = authenticate(username=request.POST.get('login'), password=request.POST.get('password'))
        if profile:
            login(request, profile)
            return HttpResponseRedirect('/torrup/')
        else:
            return render_to_response('authentification_form.html', {'show_form':True,
                                                                     'message':'Неверно введен логин или пароль.'})
    # Показываем просто форму без сообщения, если это первый раз
    else:
        return render_to_response('authentification_form.html', {'show_form':True})

# Основная страциа пользователя: список трекеров
def main_page(request):
    return render_to_response('trackers_topics.html')
    
