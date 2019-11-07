from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import ArtistViewSet, ArtViewSet, CollaboViewSet, PingView

router = DefaultRouter()
router.register('artists', ArtistViewSet, basename='artists')
router.register('arts', ArtViewSet, basename='arts')
router.register('collabos', CollaboViewSet, basename='collabos')

urlpatterns = [
    path('ping/', PingView.as_view()),
    path('', include(router.urls)),
]
