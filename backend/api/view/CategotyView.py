from rest_framework import generics
from api.serializers import CategorySerializer
from core.models import Category
from api.tasks import model


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        model.delay()
        return self.list(request, *args, **kwargs)


class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
