from django.conf.urls import url

from . import views # It means look into the same directory i.e. music and import views.py

app_name = 'music'

urlpatterns = [

    # /music/
    url(r'^$', views.index, name='index'),

    # /music/71<album_id>
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    # /music/71<album_id>/favorite/
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite')
]