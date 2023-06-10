from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MyDataSerializer
import json

class LoadJsonView(APIView):
    def get(self, request):
        with open('career_path_.json') as file:
            data = json.load(file)
        serializer = MyDataSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)