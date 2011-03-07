# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

import hashlib

from torrup.webinterface.models import *

# Вывод формы регистрации
def registration_form(request):
    return render_to_response('registration_form.html')
    
# Обработка заполненной формы и вывод поздравления о регистрации
@csrf_exempt
def registration(request):
    get_login = request.POST.get('login','')
    get_password1 = request.POST.get('password1','')
    get_password2 = request.POST.get('password2','')
    
    profile = Profile.objects.filter(username=get_login)
    if profile:
        return HttpResponse("Такой уже есть!")
    elif get_password1 == get_password2 and get_password1 != '' and get_password2 != '':
        profile = Profile(username=get_login)
        profile.set_password(get_password1)
        profile.save()

        return HttpResponse('OK!')
    else:
        return HttpResponse("Пароли не совпадают")

    #return HttpResponseRedirect('../registration/')
