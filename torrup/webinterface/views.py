# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

import hashlib

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
                                                             'message':'Поздравляем, вы успешно зарегистрировались.'})
    # Если пароли не одинаковые
    else:
        return render_to_response('registration_form.html', {'last_login':get_login, 
                                                             'last_password1':get_password1, 
                                                             'last_password2':get_password2,
                                                             'show_form':True, 
                                                             'message':'Пароли не совпадают.'})

    #return HttpResponseRedirect('../registration/')

# Форма аутентификации пользователя
def authentication_form(request):
    if 'login' in request.POST and 'password' in request.POST:
        # Обработать введенные логин и пароль, если правильно, то аутентифицировать пользователя
        # и перевести его на страницу с трекерами.
        # иначе вывести опять форму и вывести сообщение об ошибке.
        return HttpResponse('cablaaaam')
    else:
        return render_to_response('authentification_form.html', {'show_form':True})
    
# Основная страциа пользователя: список трекеров
def tracker_list(request):
    pass
    
