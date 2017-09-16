from django.conf.urls import url

from . import views # It means look into the same directory i.e. music and import views.py

app = 'music'

urlpatterns = [

    # /music/
    url(r'^$', views.index, name='index'),

    # /music/71
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail')
]