from django.conf.urls.defaults import *
from webinterface.views import *

urlpatterns = patterns('',
    (r'auth/registration/$', registration_form),
    (r'auth/registered/$', registration),
    (r'^(.*)media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/svart/Work/torrent-updater/torrup/webinterface/media'}),
)
