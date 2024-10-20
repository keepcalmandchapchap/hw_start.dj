from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    # TODO: задайте требуемые фильтр
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['created_at',]