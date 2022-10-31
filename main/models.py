from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя исполнителя')

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название альбома')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_year = models.PositiveIntegerField(verbose_name='Год выпуска')

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название песни')
    albums = models.ManyToManyField(Album, through='AlbumSong')

    def __str__(self):
        return self.title


class AlbumSong(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    song_number = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'Песня номер {self.song_number} с альбома {self.album}'

    class Meta:
        unique_together = ['album', 'song_number']
