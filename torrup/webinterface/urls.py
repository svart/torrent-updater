from django.conf.urls.defaults import *
from django.contrib.auth.views import logout_then_login
from webinterface.views import *

urlpatterns = patterns('',
    url(r'auth/logout/$', logout_then_login, {'login_url':'/torrup/auth/'}),
    url(r'auth/registration/$', registration_form),
    url(r'auth/registered/$', registration),
    url(r'auth/$', authentication_form),
    url(r'^$', main_page),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/svart/Work/Python/PycharmProjects/torrent-updater/torrup/webinterface/media'}),
)
