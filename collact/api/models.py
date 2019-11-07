from django.db import models
from django.db.models import Q
from django_mysql.models import ListCharField

from accounts.models import User


class Artist(models.Model):
    FIELD_IMAGE= 'image'
    FIELD_VIDEO = 'video'
    FIELD_PROGRAMMING = 'programming'
    FIELD_MUSIC = 'music'
    FIELD_PERFORMANCE = 'performance'
    FIELD_OBJECT = 'object'
    FIELD_IDEA = 'idea'
    FIELDS = (
        (FIELD_IMAGE,'image'),
        (FIELD_VIDEO, 'video'),
        (FIELD_PROGRAMMING, 'programming'),
        (FIELD_MUSIC, 'music'),
        (FIELD_PERFORMANCE, 'performance'),
        (FIELD_OBJECT, 'object'),
        (FIELD_IDEA, 'idea'),
    )

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='artist', on_delete=models.CASCADE)
    description = models.TextField(null=True)
    url = models.TextField(null=True)

    collaboration_types = ListCharField(
        base_field=models.CharField(choices=FIELDS, max_length=20),
        max_length=(20 * 7),
        null=True,
    )
    creation_type = models.CharField(choices=FIELDS, max_length=20)

    @property
    def name(self):
        return self.user.name

    @property
    def waiting_collabos(self):
        return Collabo.objects.filter(main_artist=self, status=Collabo.STATUS_WAITING)

    @property
    def working_collabos(self):
        return Collabo.objects.filter(Q(main_artist=self) | Q(sub_artist=self)).filter(status=Collabo.STATUS_WORKING)

    @property
    def completed_collabos(self):
        return Collabo.objects.filter(Q(main_artist=self) | Q(sub_artist=self)).filter(status=Collabo.STATUS_COMPLETED)

    @property
    def favorite_artists(self):
        return FavoriteArtist.objects.filter(who=self)

    @property
    def favorite_collabos(self):
        return FavoriteCollabo.objects.filter(who=self)

    @property
    def followers(self):
        return FavoriteArtist.objects.filter(favorite=self)

    @property
    def arts(self):
        return Art.objects.filter(artist=self)


class Art(models.Model):
    id = models.AutoField(primary_key=True)
    artist = models.ForeignKey(Artist, related_name='arts', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.TextField(null=True)
    thumbnail_url = models.TextField(null=True)
    url = models.TextField(null=True)
    color = models.CharField(max_length=10)

    created_dt = models.DateTimeField(auto_now_add=True, db_index=True)


class Collabo(models.Model):
    STATUS_WAITING = 'waiting'
    STATUS_WORKING = 'working'
    STATUS_COMPLETED = 'completed'
    STATUS_TYPES = (
        (STATUS_WAITING, 'waiting'),
        (STATUS_WORKING, 'working'),
        (STATUS_COMPLETED, 'completed'),
    )

    id = models.AutoField(primary_key=True)
    main_artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='+')
    sub_artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='+')
    status = models.CharField(choices=STATUS_TYPES, max_length=20, db_index=True, default=STATUS_WAITING)
    title = models.CharField(max_length=20, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    start_dt = models.DateTimeField(db_index=True, null=True)
    end_dt = models.DateTimeField(db_index=True, null=True)
    created_dt = models.DateTimeField(auto_now_add=True, db_index=True)

    @property
    def likes(self):
        return FavoriteCollabo.objects.filter(favorite=self).count()


class FavoriteArtist(models.Model):
    id = models.AutoField(primary_key=True)
    who = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='+')
    favorite = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='+')


class FavoriteCollabo(models.Model):
    id = models.AutoField(primary_key=True)
    who = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='favorite_collabos')
    favorite = models.ForeignKey(Collabo, on_delete=models.CASCADE, related_name='+')
