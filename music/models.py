# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your models here.
# MODELS.PY - Its a template of the database. How you are going to store the data

from django.db import models

class Album(models.Model):
    artist = models.CharField(max_length=250) #** max_length **
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.album_title + ' - ' + self.artist

class Song(models.Model):
    # ** models.ForeignKey **
    # ** models.CASCADE means that when any album is deleted, its associated songs are also deleted
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=250)
    song_title = models.CharField(max_length=250)

    def __str__(self):
        return self.song_title
