from rest_framework import serializers
from django.core.exceptions import ValidationError


class BaseSerializer(serializers.Serializer):

    def is_valid(self, raise_exception=False):
        if hasattr(self, 'initial_data'):
            unknown = set(self.initial_data.keys()) - set(self.fields.keys())
            if unknown:
                raise ValidationError("Unknown fields: {}".format(unknown)) 
        return super(BaseSerializer, self).is_valid(raise_exception)


class StatusSerializer(serializers.Serializer):
    status = serializers.CharField(max_length=None, required=False)


class CarSerializer(BaseSerializer):
    id = serializers.IntegerField()
    seats = serializers.IntegerField()


class JourneySerializer(BaseSerializer):
    id = serializers.IntegerField()
    people = serializers.IntegerField()


class DropOffSerializer(BaseSerializer):
    id = serializers.IntegerField()


class LocaleSerializer(BaseSerializer):
    group_id = serializers.IntegerField()
    car = CarSerializer(required=False)
