import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=70, verbose_name='Исполнитель')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Исполнитель'


def current_year():
    return datetime.date.today().year


class Album(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название альбома')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, verbose_name='Исполнитель')
    release_year = models.PositiveIntegerField(
        validators=[MinValueValidator(1920), MaxValueValidator(current_year())],
        verbose_name='Год выпуска'
    )

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название песни')
    albums = models.ManyToManyField(Album, through='AlbumSong', related_name='songs')

    def __str__(self):
        return self.title


class AlbumSong(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    song_number = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.song_number}: {self.song}'

    class Meta:
        unique_together = ['album', 'song_number']
