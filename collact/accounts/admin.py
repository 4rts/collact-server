from django.contrib import admin

from accounts.models import User
# Register your models here.


# TODO: 추후 정리 필요
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [f.name for f in User._meta.fields]
