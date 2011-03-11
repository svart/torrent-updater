from django.conf.urls.defaults import *
from webinterface.views import *

urlpatterns = patterns('',
    url(r'auth/logout/$', logout_user),
    url(r'auth/registration/$', registration_form),
    url(r'auth/registered/$', registration),
    url(r'auth/$', authentication_form),
    url(r'^$', main_page),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/svart/Work/torrent-updater/torrup/webinterface/media'}),
)
