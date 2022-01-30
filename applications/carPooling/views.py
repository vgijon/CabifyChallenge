from django.shortcuts import render

from rest_framework.generics import views
from rest_framework.response import Response

from .serializers import StatusSerializer


class StatusView(views.APIView):

    def get(self, request):        
        status = {"status": "Car Pooling Service is working"}
        results = StatusSerializer(status).data
        return Response(results)
