from rest_framework import viewsets

from main.models import Album, Artist
from main.serializers import AlbumSerializer, ArtistSerializer


class ArtistViewSet(viewsets.ModelViewSet):

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class AlbumViewSet(viewsets.ModelViewSet):

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
