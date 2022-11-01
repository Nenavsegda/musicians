from django.urls import include, path
from rest_framework.routers import DefaultRouter

from main import views

router = DefaultRouter()
router.register(r'artists', views.ArtistViewSet)
router.register(r'albums', views.AlbumViewSet)
router.register(r'songs', views.AlbumSongViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
