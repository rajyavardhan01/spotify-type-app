# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
# VIEWS.PY - takes an input from the user and responds with a web page or something

from django.http import HttpResponse
from .models import Album # for connecting to models.py database schema

def index(request):

    # Taking all the album objects from the db using class1.object.all()
    # and displaying it to the home page
    all_albums = Album.objects.all()

    # Creating hyperlinks for each Album object using its id ie. for each Album
    # and then displaying them on the page
    html=''
    for album in all_albums:
        url = '/music/' + str(album.id) + '/'
        html += '<a href="' + url + '">' + album.album_title + '</a><br>'

    return HttpResponse(html)

def detail(request, album_id):
    return HttpResponse('<h2> Details for album id ' + str(album_id) + '</h2>')