from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import ArtistViewSet, ArtViewSet, CollaboViewSet, PingView, FavoriteArtistViewSet, \
    FavoriteCollaboViewSet, CollaboRegisterView, CollaboApplicationViewSet

router = DefaultRouter()
router.register('artists', ArtistViewSet, basename='artists')
router.register('arts', ArtViewSet, basename='arts')
router.register('collabos', CollaboViewSet, basename='collabos')
router.register('collabo_applications', CollaboApplicationViewSet, basename='collabo_applications')
router.register('favorite_artists', FavoriteArtistViewSet, basename='favorite_artists')
router.register('favorite_collabos', FavoriteCollaboViewSet, basename='favorite_collabos')

urlpatterns = [
    path('ping/', PingView.as_view()),
    path('collabos/register', CollaboRegisterView.as_view()),
    path('', include(router.urls)),
]
