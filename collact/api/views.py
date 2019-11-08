from django.db.models import Q
from django_filters import rest_framework as filters
from requests import Response
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework_serializer_extensions.views import SerializerExtensionsAPIViewMixin

from api.filters import PrimaryKeyFilter
from api.models import Artist, Art, Collabo, FavoriteArtist, FavoriteCollabo, CollaboApplication
from api.serializers import ArtistSerializer, ArtSerializer, CollaboSerializer, CollaboApplicationSerializer


class DefaultViewSet(SerializerExtensionsAPIViewMixin, viewsets.GenericViewSet):
    def get_queryset(self):
        qs = super().get_queryset()
        return self.get_serializer_class().prepare_queryset(qs, context=self.get_serializer_context())

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({
            'request': self.request,
            'view': self,
        })
        return context


class PingView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        return Response('pong')


class ArtistViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    DefaultViewSet):
    queryset = Artist.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ArtistSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    filter_backends = (PrimaryKeyFilter, filters.DjangoFilterBackend)


class ArtViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    DefaultViewSet):
    queryset = Art.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ArtSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    filter_backends = (PrimaryKeyFilter, filters.DjangoFilterBackend)


class CollaboApplicationViewSet(mixins.ListModelMixin,
                                mixins.CreateModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.DestroyModelMixin,
                                DefaultViewSet):
    queryset = CollaboApplication.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CollaboApplicationSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    filter_backends = (PrimaryKeyFilter, filters.DjangoFilterBackend)


class CollaboFilterSet(filters.FilterSet):
    main_artist = filters.CharFilter(method='main_artist_method')
    artist = filters.CharFilter(method='artist_method')
    status = filters.CharFilter(method='status_method')

    @staticmethod
    def main_artist_method(queryset, _, value):
        return queryset.filter(main_artist__in=value.split(','))

    @staticmethod
    def artist_method(queryset, _, value):
        return queryset.filter(Q(main_artist=value) | Q(sub_artist=value))

    @staticmethod
    def status_method(queryset, _, value):
        return queryset.filter(status__in=value.split(','))


class CollaboViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    DefaultViewSet):
    queryset = Collabo.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CollaboSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    filter_backends = (PrimaryKeyFilter, filters.DjangoFilterBackend)


class FavoriteArtistViewSet(mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            DefaultViewSet):
    queryset = FavoriteArtist.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CollaboSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    filter_backends = (PrimaryKeyFilter, filters.DjangoFilterBackend)


class FavoriteCollaboViewSet(mixins.ListModelMixin,
                             mixins.CreateModelMixin,
                             mixins.RetrieveModelMixin,
                             mixins.UpdateModelMixin,
                             mixins.DestroyModelMixin,
                             DefaultViewSet):
    queryset = FavoriteCollabo.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CollaboSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    filter_backends = (PrimaryKeyFilter, filters.DjangoFilterBackend)
