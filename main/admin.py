from django.contrib import admin
from main.models import Artist, Album, Song, AlbumSong

class AlbumSongInline(admin.TabularInline):
    model = Song.albums.through


class AlbumAdmin(admin.ModelAdmin):
    inlines = [AlbumSongInline,]


class SongAdmin(admin.ModelAdmin):
    inlines = [AlbumSongInline,]
    exclude = ('album',)

admin.site.register(Song, SongAdmin)
admin.site.register(AlbumSong)
admin.site.register(Artist)
admin.site.register(Album, AlbumAdmin)

