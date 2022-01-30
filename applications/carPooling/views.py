from rest_framework import status
from rest_framework.generics import views
from rest_framework.response import Response

from applications.carPooling.serializers import StatusSerializer, CarSerializer, JourneySerializer, DropOffSerializer


class StatusView(views.APIView):

    def get(self, request):        
        status = {"status": "Car Pooling Service is working"}
        results = StatusSerializer(status).data
        return Response(results)


class LoadCarsView(views.APIView):

    def put(self, request):              
        serializer = CarSerializer(data=request.data, many=True)
        if serializer.is_valid():
            # Delete cars and journeys
            # Save new list of cars
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class BookingJourneyView(views.APIView):

    def post(self, request):
        serializer = JourneySerializer(data=request.data)
        if serializer.is_valid():
            # Registry group in journey queue
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DropOffJourneyView(views.APIView):

    def post(self, request):
        serializer = DropOffSerializer(data=request.data)
        if serializer.is_valid():
            # if group_id exists
                return Response(status=status.HTTP_200_OK)
            # else
                #return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
