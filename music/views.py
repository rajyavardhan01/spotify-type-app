# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Album # for connecting to models.py database schema

from django.shortcuts import render, get_object_or_404

def index(request):

    all_albums = Album.objects.all()

    context = {'all_albums': all_albums}  # NOTE: context is a dictionary of Album objects

    return render(request, 'music/index.html', context)

def detail(request, album_id):

    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})