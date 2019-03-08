from django.conf.urls import url
from .views import list, create, detail, update, delete

urlpatterns = [

    url('^$', list, name='list'),
    url('^create/$', create, name='create'),
    url('^(?P<id>\d+)/$', detail, name='detail'),
    url('^(?P<id>\d+)/update/$', update, name='update'),
    url('^(?P<id>\d+)/delete/$', delete, name='delete'),
]
