from rest_framework import viewsets

from main.models import Album, AlbumSong, Artist
from main.serializers import (AlbumSongSerializer, DetailAlbumSerializer,
                              DetailArtistSerializer, ListAlbumSerializer,
                              ListArtistSerializer)


class ArtistViewSet(viewsets.ModelViewSet):

    serializer_class = ListArtistSerializer
    queryset = Artist.objects.all()
    detail_serializer_class = DetailArtistSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class

        return super(ArtistViewSet, self).get_serializer_class()


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = ListAlbumSerializer
    detail_serializer_class = DetailAlbumSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super(AlbumViewSet, self).get_serializer_class()

    def perform_update(self, serializer):
        artist_instance, _ = Artist.objects.get_or_create(
            name=self.request.data['artist']
        )
        serializer.save(artist=artist_instance)


class AlbumSongViewSet(viewsets.ModelViewSet):
    queryset = AlbumSong.objects.all()
    serializer_class = AlbumSongSerializer
