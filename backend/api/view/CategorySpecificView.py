from rest_framework import generics
from api.serializers import CategorySpecificSerializer
from core.models import CategorySpecific


class CategorySpecificListView(generics.ListAPIView):
    queryset = CategorySpecific.objects.all()
    serializer_class = CategorySpecificSerializer
    filter_fields = ('parent', 'parent_id')

    def get_queryset(self):
        return self.queryset.filter(parent_id=self.request.query_params['parent_id'])

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CategorySpecificCreateView(generics.CreateAPIView):
    queryset = CategorySpecific.objects.all()
    serializer_class = CategorySpecificSerializer
