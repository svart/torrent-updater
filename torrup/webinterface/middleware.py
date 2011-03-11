# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
import re

class AuthMiddleware(object):
    def process_request(self, request):
        # Если обращение идет к медиа-файлам, то не нужно фильтровать
        prog = re.compile(r'^/torrup/media/.*')
        if prog.match(request.path):
            pass
        else:
            if request.path not in ["/torrup/auth/", "/torrup/auth/registration/", "/torrup/auth/registered/"]:
                if request.user.is_authenticated():
                    pass
                else:
                    return HttpResponseRedirect('/torrup/auth/')
            # Если пользователь авторизирован, но хочет зайти на форму регистрации или авторизации,
            # то он перенаправляется на главную страницу.
            elif request.user.is_authenticated():
                return HttpResponseRedirect('/torrup/')
    
