from collections import defaultdict

from django.db.models import QuerySet
from rest_framework import serializers
from rest_framework_serializer_extensions.serializers import SerializerExtensionsMixin


class PrepareModelSerializer(SerializerExtensionsMixin, serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.many_to_one_cache = {}
        self.one_to_many_cache = {}

    @classmethod
    def prepare_queryset(cls, qs, context=None):
        return qs

    def get_cached_many_to_one(self, field_name, serializer_class):
        """
        Many-to-One일 경우에만 사용
        예를 들어 AlertSerializer에서 patient field를 넣고 싶은 경우,
        먼저 대상 alert들에서 patient_id들을 각각 가져와서 list를 만들고 이걸로 patient list를 만든다.
        이렇게 하면 alert 하나하나마다 patient table에 select를 하는 것을 방지할 수 있다.

        :param field_name: foreignkey relation name (예: alert.patient -> patient)
        :param serializer_class: (예: alert.patient -> PatientSerializer)
        :return: id -> object mapping (예: patient_id -> serialized patient)
        """
        if field_name not in self.many_to_one_cache:
            if isinstance(self.instance, (QuerySet, list)):
                ids = [getattr(obj, f'{field_name}_id') for obj in self.instance]
            else:
                ids = [getattr(self.instance, f'{field_name}_id')]

            qs = serializer_class.Meta.model.objects.filter(id__in=ids)
            serializer = serializer_class(serializer_class.prepare_queryset(qs), many=True)
            self.many_to_one_cache[field_name] = {x['id']: x for x in serializer.data}

        return self.many_to_one_cache[field_name]

    def get_cached_one_to_many(self, field_name, serializer_class):
        """
        One-to-Many일 경우에만 사용
        :param field_name: (예: patient.alerts -> patient)
        :param serializer_class: (예: patient.alerts -> AlertSerializer)
        :return: id -> list of object mapping (예: patient id -> list of serialized alerts)
        """
        if field_name not in self.one_to_many_cache:
            if isinstance(self.instance, (QuerySet, list)):
                ids = [obj.id for obj in self.instance]
            else:
                ids = [self.instance.id]

            qs = serializer_class.Meta.model.objects.filter(**{f'{field_name}_id__in': ids})
            serializer = serializer_class(serializer_class.prepare_queryset(qs), many=True)
            self.one_to_many_cache[field_name] = defaultdict(list)
            for serialized_obj in serializer.data:
                self.one_to_many_cache[field_name][serialized_obj[field_name]].append(serialized_obj)

        return self.one_to_many_cache[field_name]
