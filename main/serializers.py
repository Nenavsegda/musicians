from rest_framework import serializers

from main.models import Album, AlbumSong, Artist


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['name']


class ListAlbumSerializer(serializers.ModelSerializer):
    artist = serializers.StringRelatedField()

    class Meta:
        model = Album
        fields = ['id', 'title', 'artist', 'release_year']


class DetailAlbumSerializer(serializers.ModelSerializer):
    artist = serializers.StringRelatedField()
    songs = serializers.SerializerMethodField()

    def get_songs(self, obj):
        song_order = AlbumSong.objects.filter(album=obj)
        return [f'{song}' for song in song_order]

    class Meta:
        model = Album
        fields = ['id', 'title', 'artist', 'release_year', 'songs']
