from rest_framework import serializers
from core.models import ImagePath, ResNet, Category, CategorySpecific
from api.tasks import model


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagePath
        fields = "__all__"


class ResnetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResNet
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

    def create(self, validated_data):
        instance = super().create(validated_data)
        model.delay(instance.category)
        return instance


class CategorySpecificSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategorySpecific
        fields = "__all__"

    def create(self, validated_data):
        instance = super().create(validated_data)
        model.delay(instance.category)
        return instance
