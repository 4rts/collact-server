from rest_framework.filters import BaseFilterBackend


class PrimaryKeyFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        ids = request.query_params.get('ids', None)
        if ids is None:
            return queryset
        ids = ids.split(',')
        return queryset.filter(id__in=ids)
