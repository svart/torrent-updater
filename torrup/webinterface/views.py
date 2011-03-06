# -*- coding: utf-8 -*-
from torrup.webinterface.models import *

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

# Вывод формы регистрации
def registration_form(request):
    return render_to_response('registration_form.html')
    
# Обработка заполненной формы и вывод поздравления о регистрации
def registration(request):
    return HttpResponseRedirect('../registration/')
