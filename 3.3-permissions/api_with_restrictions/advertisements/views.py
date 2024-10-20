from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import  DjangoFilterBackend
from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from advertisements.permissions import IsOwnerOrReadOnly, OnlyDelete
from advertisements.filters import AdvertisementFilter

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = [AdvertisementFilter]
    filterset_fields = ['creator', 'status']
    

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update",]:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        elif self.action == 'destroy':
            return [IsAuthenticated(), OnlyDelete()]
        return []
