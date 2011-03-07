from django.conf.urls.defaults import *
from webinterface.views import *

urlpatterns = patterns('',
    url(r'auth/registration/$', registration_form),
    url(r'auth/registered/$', registration),
    
    url(r'^(.*)media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/svart/Work/torrent-updater/torrup/webinterface/media'}),
)
