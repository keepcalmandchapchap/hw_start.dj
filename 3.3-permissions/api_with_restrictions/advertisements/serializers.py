from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ValidationError

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""
        # TODO: добавьте требуемую валидацию
        user = self.context['request'].user
        advertisements_with_open = Advertisement.objects.filter(creator=user, status='OPEN').count()
        if advertisements_with_open >= 10:
            if self.context['request']._request.method == 'POST':
                raise ValidationError(f'''Превышен лимит записей со статусом OPEN у пользователя {user}, кол-во записей {advertisements_with_open}''')
            elif self.context['request']._request.method == 'PATCH' and data.get('status') == 'OPEN':
                raise ValidationError(f'''Превышен лимит записей со статусом OPEN у пользователя {user}, кол-во записей {advertisements_with_open}''')    

        return data
