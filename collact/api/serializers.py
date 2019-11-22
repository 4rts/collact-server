from rest_framework import serializers

from api.models import Artist, Art, Collabo, FavoriteArtist, FavoriteCollabo, CollaboApplication
from main.utils.serializers import PrepareModelSerializer


class ArtistSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'user', 'profile', 'name')


class CollaboSimpleSerializer(serializers.ModelSerializer):
    main_artist = serializers.SerializerMethodField()
    sub_artist = serializers.SerializerMethodField()

    class Meta:
        model = Collabo
        fields = ('id', 'file', 'main_artist', 'sub_artist')

    @staticmethod
    def get_main_artist(collabo):
        return ArtistSimpleSerializer(collabo.main_artist).data

    @staticmethod
    def get_sub_artist(collabo):
        return ArtistSimpleSerializer(collabo.sub_artist).data

##################


class ArtSerializer(PrepareModelSerializer):
    class Meta:
        model = Art
        exclude = ()
        read_only_fields = ('id',)


class CollaboApplicationSerializer(PrepareModelSerializer):
    class Meta:
        model = CollaboApplication
        exclude = ()
        read_only_fields = ('id',)


class CollaboSerializer(PrepareModelSerializer):
    class Meta:
        model = Collabo
        fields = ('id', 'main_artist', 'sub_artist', 'status', 'title', 'description',
                  'application', 'start_dt', 'end_dt', 'created_dt', 'likes', 'file')
        read_only_fields = ('id',)
        expandable_fields = {
            'main_artist': {'serializer': ArtistSimpleSerializer},
            'sub_artist': {'serializer': ArtistSimpleSerializer},
        }


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
    favorite_artists = serializers.SerializerMethodField()
    favorite_collabos = serializers.SerializerMethodField()

    waiting_collabos = serializers.SerializerMethodField()
    working_collabos = serializers.SerializerMethodField()
    completed_collabos = serializers.SerializerMethodField()

    followers = serializers.SerializerMethodField()

    class Meta:
        model = Artist
        fields = ('id', 'user', 'description', 'profile', 'collaboration_types', 'creation_type',
                  'arts', 'name', 'favorite_artists', 'favorite_collabos',
                  'waiting_collabos', 'working_collabos', 'completed_collabos', 'followers')
        read_only_fields = ('id',)
        expandable_fields = {
            'arts': {'serializer': ArtSerializer, 'many': True},
        }

    @staticmethod
    def get_favorite_artists(artist):
        return ArtistSimpleSerializer(artist.favorite_artists, many=True).data

    @staticmethod
    def get_favorite_collabos(artist):
        return CollaboSimpleSerializer(artist.favorite_collabos, many=True).data

    @staticmethod
    def get_waiting_collabos(artist):
        return CollaboSimpleSerializer(artist.waiting_collabos, many=True).data

    @staticmethod
    def get_working_collabos(artist):
        return CollaboSimpleSerializer(artist.working_collabos, many=True).data

    @staticmethod
    def get_completed_collabos(artist):
        return CollaboSimpleSerializer(artist.completed_collabos, many=True).data

    @staticmethod
    def get_followers(artist):
        return ArtistSimpleSerializer(artist.followers, many=True).data
