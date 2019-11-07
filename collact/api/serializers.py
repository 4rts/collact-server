from api.models import Artist, Art, Collabo, FavoriteArtist, FavoriteCollabo
from main.utils.serializers import PrepareModelSerializer


class ArtSerializer(PrepareModelSerializer):
    class Meta:
        model = Art
        exclude = ()
        read_only_fields = ('id',)


class CollaboSerializer(PrepareModelSerializer):
    class Meta:
        model = Collabo
        fields = ('id', 'main_artist', 'sub_artist', 'status', 'title', 'description',
                  'start_dt', 'end_dt', 'created_dt', 'likes')
        read_only_fields = ('id',)


class FavoriteArtistSerializer(PrepareModelSerializer):
    class Meta:
        model = FavoriteArtist
        exclude = ()
        read_only_fields = ('id',)


class FavoriteCollaboSerializer(PrepareModelSerializer):
    class Meta:
        model = FavoriteCollabo
        exclude = ()
        read_only_fields = ('id',)


class ArtistSerializer(PrepareModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'user', 'description', 'url', 'collaboration_types', 'creation_type',
                  'arts', 'favorite_artists', 'favorite_collabos',
                  'name', 'waiting_collabos', 'working_collabos', 'completed_collabos', 'followers')
        read_only_fields = ('id',)
        expandable_fields = {
            'favorite_collabos': {'serializer': CollaboSerializer, 'many': True},
            'waiting_collabos': {'serializer': CollaboSerializer, 'many': True},
            'working_collabos': {'serializer': CollaboSerializer, 'many': True},
            'completed_collabos': {'serializer': CollaboSerializer, 'many': True},
        }
