from rest_framework import serializers
from .models import Ad, Comment


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою

class CommentSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    pass


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdDetailSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    # author_last_name = ''
    # author_id = ''
    # def get_author_first_name(self, obj):
        # return obj.author.first_name

    class Meta:
        model = Ad
        fields = '__all__'
