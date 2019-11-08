from django.db import models
from django.utils import timezone


class SoftDeletionQuerySet(models.QuerySet):
    def delete(self):
        now = timezone.now()
        updated_rows = super().update(deleted_dt=now, updated_dt=now)
        return bool(updated_rows), updated_rows

    def hard_delete(self):
        return super().delete()


class SoftDeletionManager(models.Manager):
    """
    RedisCacheManager 등 여러 manager들과 함께 상속될 땐
    항상 맨 마지막에 들어가야 super()가 models.Manager를 가리키게 됨
    """
    queryset_class = SoftDeletionQuerySet

    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        super().__init__(*args, **kwargs)

    def get_queryset(self):
        if self.alive_only:
            return self.queryset_class(self.model).filter(deleted_dt=None)
        return self.queryset_class(self.model)


class SoftDeletionModel(models.Model):
    """
    RedisCacheModel 등 여러 model들과 함께 상속될 땐
    항상 맨 마지막에 들어가야 super()가 models.Model을 가리키게 됨
    """
    deleted_dt = models.DateTimeField(blank=True, null=True, db_index=True)

    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)

    def delete(self):
        self.deleted_dt = timezone.now()
        super().save()

    def hard_delete(self):
        super().delete()

    class Meta:
        abstract = True
