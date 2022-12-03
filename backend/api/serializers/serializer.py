from rest_framework import serializers
from core.models import ImagePath, ResNet


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagePath
        fields = "__all__"


class ResnetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResNet
        fields = "__all__"
