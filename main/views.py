from rest_framework import viewsets
from rest_framework.response import Response

from main.models import Album, Artist, Song
from main.serializers import ArtistSerializer, \
    DetailAlbumSerializer, ListAlbumSerializer


class ArtistViewSet(viewsets.ModelViewSet):

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class AlbumViewSet(viewsets.ModelViewSet):

    serializer_class = ListAlbumSerializer
    queryset = Album.objects.all()
    detail_serializer_class = DetailAlbumSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class

        return super(AlbumViewSet, self).get_serializer_class()
