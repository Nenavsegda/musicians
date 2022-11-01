from rest_framework import serializers

from main.models import Album, AlbumSong, Artist


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['name']


class ListAlbumSerializer(serializers.ModelSerializer):
    artist = serializers.CharField(max_length=50)

    def create(self, validated_data):
        artist_name = validated_data.pop('artist')
        artist_instance, _ = Artist.objects.get_or_create(name=artist_name)
        obj = Album.objects.create(**validated_data, artist=artist_instance)
        return obj

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
