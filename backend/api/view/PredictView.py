from rest_framework.views import APIView
from rest_framework.response import Response


class PredictView(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data['image'])
        return Response()
