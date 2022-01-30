from rest_framework import serializers


class StatusSerializer(serializers.Serializer):
    status = serializers.CharField(max_length=None)


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    seats = serializers.IntegerField()


class JourneySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    people = serializers.IntegerField()


class DropOffSerializer(serializers.Serializer):
    id = serializers.IntegerField()