import decimal
from propertyapp.config.configuration import Configuration
from propertyapp.common.constants import Constants
from propertyapp.models import PropertyModel
from rest_framework import serializers
from django.db import models
import math

# Serializer class to serialize the PropertyModel class


class PropertySerializer(serializers.ModelSerializer):
    distance = serializers.SerializerMethodField('get_distance')

    def get_distance(self, obj):
        latitude = decimal.Decimal(self.context.get("latitude"))
        longitude = decimal.Decimal(self.context.get("longitude"))
        distance = calculate_distance(
            lat1=latitude, long1=longitude, lat2=obj.latitude, long2=obj.longitude)
        return round(distance, 3)

    class Meta:
        model = PropertyModel
        fields = '__all__'


# private methods
# https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude

def calculate_distance(lat1, long1, lat2, long2):
    dlat = math.radians(lat2-lat1)
    dlon = math.radians(long2-long1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = Constants.EARCH_RADIUS_KM * c
    if Configuration.DISTANCE_UNIT == Constants.METER:
        d = d * 1000
    return d
