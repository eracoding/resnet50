from rest_framework import generics
from api.serializers import ImageSerializer
from core.models import ImagePath


class ImageListView(generics.ListAPIView):
    queryset = ImagePath.objects.all()
    serializer_class = ImageSerializer


class ImageCreateView(generics.CreateAPIView):
    queryset = ImagePath.objects.all()
    serializer_class = ImageSerializer

