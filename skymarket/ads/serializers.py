from phonenumber_field import serializerfields
from rest_framework import serializers
from .models import Ad, Comment


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою

class CommentSerializer(serializers.ModelSerializer):
    ad = serializers.SlugRelatedField(read_only=True, slug_field="title")
    author = serializers.CharField(source='author.first_name', read_only=True)
    author_first_name = serializers.CharField(read_only=True, source="author_first_name")
    author_last_name = serializers.CharField(read_only=True, source="author_last_name")
    author_id = serializers.IntegerField(source='author.id', read_only=True)
    author_image = serializers.ImageField(source='author.image', read_only=True)
    ad_id = serializers.CharField(source='ad.id', read_only=True)

    class Meta:
        model = Comment
        fields = (
            "pk",
            "text",
            "author_id",
            "ad_id",
            "author_first_name",
            "author_last_name",
            "created_at",
            "author_image",
        )


class AdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ad
        fields = ("pk", "image", "title", "price", "description")


class AdDetailSerializer(serializers.ModelSerializer):
    author_first_name = serializers.ReadOnlyField(source="author.first_name")
    author_last_name = serializers.ReadOnlyField(source="author.last_name")
    phone = serializerfields.PhoneNumberField(source="author.phone", read_only=True)
    author_id = serializers.ReadOnlyField(source="author.id")

    class Meta:
        model = Ad
        fields = ("pk", "image", "title", "price", "phone", "author_first_name", "author_last_name", "description", "author_id")
