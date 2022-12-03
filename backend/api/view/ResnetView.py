from rest_framework import generics
from api.serializers import ResnetSerializer
from core.models import ResNet


class ResnetListView(generics.ListAPIView):
    queryset = ResNet.objects.all()
    serializer_class = ResnetSerializer
