from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main import views

router = DefaultRouter()
router.register(r'artists', views.ArtistViewSet)
router.register(r'albums', views.AlbumViewSet)

urlpatterns = [
    path('', include(router.urls)),
]