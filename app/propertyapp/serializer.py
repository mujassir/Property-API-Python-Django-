import decimal
from propertyapp.models import propertyModel
from rest_framework import serializers
from django.db import models
import math


class propertySerializer(serializers.ModelSerializer):
    distance = serializers.SerializerMethodField('get_distance')

    def get_distance(self, obj):
        latitude = decimal.Decimal(self.context.get("latitude"))
        longitude = decimal.Decimal(self.context.get("longitude"))
        distance = calculate_distance(
            lat1=latitude, long1=longitude, lat2=obj.latitude, long2=obj.longitude)
        return distance

    class Meta:
        model = propertyModel
        fields = '__all__'


# private methods
# https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude

def calculate_distance(lat1, long1, lat2, long2):
    radius = 6371.0  # Earth radius in km
    dlat = math.radians(lat2-lat1)
    dlon = math.radians(long2-long1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c
    return d
