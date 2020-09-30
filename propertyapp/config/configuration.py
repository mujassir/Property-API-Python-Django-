from django.db import models

# Configuration to be used in the application

class Configuration(models.Model):
    MAX_RECORD_COUNT = 100  # 10000
    APIKEYS = ["ce9d77b308c149d5992a80073637e4d5",
               "ce9d77b308c149d5992a80073637e4d6"]
    REQUIRED_PARAMETERS = ["APIKEY", "latitude", "longitude",
                           "distance", "ad_operation", "ad_typology", "ad_owner_type"]
    ORDER_OPTIONS = ["rooms", "price", "distance"]
    SORT_OPTIONS = ["asc", "desc"]
    ORDER_OPTION_ROOM = "rooms"
    ORDER_OPTION_ROOM_COLUMN_NAME = "ad_characteristics_roomNumber"
    DISTANCE_UNIT = "Meter"

