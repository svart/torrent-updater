# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect

class AuthMiddleware(object):
    def process_request(self, request):
        if request.path not in ["/torrup/auth/", "/torrup/auth/registration/", "/torrup/auth/registered/"]:
            if request.user.is_authenticated():
                pass
            else:
                return HttpResponseRedirect('/torrup/auth/')
    
