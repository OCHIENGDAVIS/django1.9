from django.conf.urls import url
from .views import index, create, detail, update, delete

urlpatterns = [

    url('^$', index, name='index'),
    url('^create/$', create, name='create'),
    url('^detail/$', detail, name='detail'),
    url('^update/$', update, name='update'),
    url('^delete/$', delete, name='delete'),
]
