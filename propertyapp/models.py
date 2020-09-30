from propertyapp.common.constants import Constants
from propertyapp.config.configuration import Configuration
from propertyapp.config.error_reason import ErrorReason
from django.http import request
from propertyapp.common.distance_manager import DistanceManager
from django.db import models

# Property model that is used to send records in the response


class PropertyModel(models.Model):
    class Meta:
        db_table = 'PROPERTY_DETAILS'

    objects2 = DistanceManager()

    # primary key
    index_key = models.IntegerField(primary_key=True)

    # number fields
    location_exact = models.BooleanField()
    # latitude = models.DecimalField(max_digits=9, decimal_places=6)
    # longitude = models.DecimalField(max_digits=9, decimal_places=6)

    latitude = models.FloatField()
    longitude = models.FloatField()

    price = models.IntegerField()
    price_down = models.IntegerField()
    price_percen = models.IntegerField()

    # string fields
    urlid = models.CharField(max_length=10)
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    daystamp = models.CharField(max_length=255)
    timestamp = models.CharField(max_length=255)
    image_01 = models.CharField(max_length=255)
    image_02 = models.CharField(max_length=255)
    image_03 = models.CharField(max_length=255)
    advertiser_firstname = models.CharField(max_length=255)
    advertiser_name = models.CharField(max_length=255)
    phonenumber_0 = models.CharField(max_length=255)
    phonenumber_1 = models.CharField(max_length=255)
    stats_date_act = models.CharField(max_length=255)
    ad_address_locationId = models.CharField(max_length=255)
    ad_address_municipalityId = models.CharField(max_length=255)
    ad_address_provinceId = models.CharField(max_length=255)
    ad_energyCertification_suffix = models.CharField(max_length=255)
    ad_energyCertification_type = models.CharField(max_length=255)
    ad_id = models.CharField(max_length=255)
    ad_owner_commercialId = models.CharField(max_length=255)
    ad_origin = models.CharField(max_length=255)
    ad_characteristics_hasGarden = models.CharField(max_length=255)
    comment = models.CharField(max_length=4000)
    location_tree = models.CharField(max_length=255)
    location_zone = models.CharField(max_length=255)
    charac_basic = models.CharField(max_length=255)
    charac_equip = models.CharField(max_length=255)

    # number fields
    ad_address_locationLevel = models.IntegerField()
    ad_characteristics_bathNumber = models.IntegerField()
    ad_characteristics_constructedArea = models.IntegerField()
    ad_characteristics_roomNumber = models.IntegerField()
    ad_media_photoNumber = models.IntegerField()
    ad_media_videoNumber = models.IntegerField()
    ad_operation = models.IntegerField()
    ad_owner_contactPreference = models.IntegerField()
    ad_owner_type = models.IntegerField()
    ad_price = models.IntegerField()
    ad_typology = models.IntegerField()
    ad_builtType = models.IntegerField()

    # boolean fields
    ad_characteristics_hasParking = models.BooleanField()
    ad_characteristics_hasSwimmingPool = models.BooleanField()
    ad_characteristics_hasTerrace = models.BooleanField()

# Property input mode is used to get POST parameters and performs validation


class PropertyInputModel(models.Model):

    # Required Parameters

    APIKEY = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    distance = models.FloatField()
    ad_operation = models.IntegerField()
    ad_typology = models.IntegerField()
    ad_owner_type = models.IntegerField()

    # Optional Parameters

    minPrice = models.FloatField()
    maxPrice = models.FloatField()
    order = models.CharField(max_length=10)
    sort = models.CharField(max_length=4)

    # Validation Attributes
    error_reason = models.IntegerField()
    is_valid = models.BooleanField()
    missing_parameters = models.CharField(max_length=255)

    @classmethod
    def create(cls, params):

        # Required Parameters

        APIKEY = params.get('APIKEY')
        latitude = params.get('latitude')
        longitude = params.get('longitude')
        distance = params.get('distance')
        ad_operation = params.get('ad_operation')
        ad_typology = params.get('ad_typology')
        ad_owner_type = params.get('ad_owner_type')

        # Optional Parameters

        minPrice = params.get('minPrice')
        maxPrice = params.get('maxPrice')
        order = params.get('order')
        sort = params.get('sort')

        # Validation Attributes

        is_valid = True
        error_reason = ErrorReason.NoReason
        missing_parameters = ""

        for param in Configuration.REQUIRED_PARAMETERS:
            if params.get(param) is None:
                is_valid = False
                error_reason = ErrorReason.RequiredParametersMissing
                missing_parameters = missing_parameters + "," + param

        if missing_parameters.startswith(","):
            missing_parameters = missing_parameters.lstrip(",")

        if not (order is None):
            if not Configuration.ORDER_OPTIONS.__contains__(order):
                is_valid = False
                error_reason = ErrorReason.OrderAttributeNotFound

        # Convert input (meters) to KMs

        if Configuration.DISTANCE_UNIT == Constants.METER:
            distance = distance / 1000

        obj = cls(APIKEY=APIKEY, latitude=latitude, longitude=longitude, distance=distance, ad_operation=ad_operation, ad_typology=ad_typology,
                  ad_owner_type=ad_owner_type, minPrice=minPrice, maxPrice=maxPrice, order=order, sort=sort, is_valid=is_valid, error_reason=error_reason, missing_parameters=missing_parameters)
        return obj
