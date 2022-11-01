from rest_framework import serializers

from main.models import Album, AlbumSong, Artist, Song


class ListArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['name']


class DetailArtistSerializer(serializers.ModelSerializer):
    albums = serializers.SerializerMethodField()

    def get_albums(self, obj):
        return [f'{album}' for album in obj.albums.all()]

    class Meta:
        model = Artist
        fields = ['name', 'albums']


class ListAlbumSerializer(serializers.HyperlinkedModelSerializer):
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


class AlbumSongSerializer(serializers.ModelSerializer):
    album = serializers.CharField(max_length=50)
    song = serializers.CharField(max_length=50)

    def to_representation(self, instance):
        self.fields['album'] = serializers.StringRelatedField()
        self.fields['song'] = serializers.StringRelatedField()
        return super(AlbumSongSerializer, self).to_representation(instance)

    def create(self, validated_data):
        album_title = validated_data.pop('album')
        song_title = validated_data.pop('song')
        album_instance = Album.objects.filter(title=album_title).first()
        if not album_instance:
            raise serializers.ValidationError("Такого альбома не существует")
        song_instance, _ = Song.objects.get_or_create(title=song_title)
        obj = AlbumSong.objects.create(
            **validated_data, album=album_instance, song=song_instance
        )
        return obj

    class Meta:
        model = AlbumSong
        fields = '__all__'
