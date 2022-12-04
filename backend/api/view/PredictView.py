from rest_framework.views import APIView
from rest_framework.response import Response

from api.neuron_model import ResNetUltra
from core.models import ResNet, Category, CategorySpecific


class PredictView(APIView):
    def post(self, request, *args, **kwargs):
        my_file = request.data["image"]
        with open(f"/tmp/{my_file.name}", "wb+") as destination:
            for chunk in my_file.chunks():
                destination.write(chunk)
        resnet = ResNetUltra()
        try:
            category_name = resnet.netPredict(model=ResNet.objects.last(), gimage=f"/tmp/{my_file.name}")
            category = Category.objects.filter(category__contains=category_name).first()
            if category is None:
                specific = CategorySpecific.objects.filter(category__contains=category_name).first()
                category = specific.parent
            return Response(
                {'category': category.category})
        except:
            return Response(
                {
                    'category': "Not found"
                }
            )
