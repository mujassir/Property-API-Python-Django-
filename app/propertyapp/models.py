from propertyapp.distance_manager import DistanceManager
from django.db import models


class propertyModel(models.Model):
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
    comment = models.CharField(max_length=255)
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
