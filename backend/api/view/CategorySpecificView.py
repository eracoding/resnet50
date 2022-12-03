from rest_framework import generics
from api.serializers import CategorySpecificSerializer
from core.models import CategorySpecific


class CategorySpecificListView(generics.ListAPIView):
    queryset = CategorySpecific.objects.all()
    serializer_class = CategorySpecificSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CategorySpecificCreateView(generics.CreateAPIView):
    queryset = CategorySpecific.objects.all()
    serializer_class = CategorySpecificSerializer
