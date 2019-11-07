from django.contrib import admin

# Register your models here.
from api.models import Artist, Art, Collabo, FavoriteArtist, FavoriteCollabo


# TODO: 추후 정리 필요
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Artist._meta.fields]


@admin.register(Art)
class ArtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Art._meta.fields]


@admin.register(Collabo)
class CollaboAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Collabo._meta.fields]


@admin.register(FavoriteArtist)
class FavoriteArtistAdmin(admin.ModelAdmin):
    list_display = [f.name for f in FavoriteArtist._meta.fields]


@admin.register(FavoriteCollabo)
class FavoriteCollaboAdmin(admin.ModelAdmin):
    list_display = [f.name for f in FavoriteCollabo._meta.fields]
