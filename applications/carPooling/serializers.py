from rest_framework import serializers


class StatusSerializer(serializers.Serializer):
    status = serializers.CharField(max_length=None)


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    seats = serializers.IntegerField()
