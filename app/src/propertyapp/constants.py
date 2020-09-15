import enum
from django.db import models

# Constants to be used in the application

class Constants(models.Model):
    MAX_RECORD_COUNT = 100  # 10000
    APIKEYS = ["ce9d77b308c149d5992a80073637e4d5",
               "ce9d77b308c149d5992a80073637e4d6"]
    REQUIRED_PARAMETERS = ["APIKEY", "latitude", "longitude",
                           "distance", "ad_operation", "ad_typology", "ad_owner_type"]
    ORDER_OPTIONS = ["rooms", "price", "distance"]
    SORT_OPTIONS = ["asc", "desc"]
    ORDER_OPTION_ROOM = "rooms"
    ORDER_OPTION_ROOM_COLUMN_NAME = "ad_characteristics_roomNumber"

# JSON Error messages to be used in the application

class ErrorMessages(models.Model):
    InvalidAPIKey = {
        "code": 401,
        "error_code": 'InvalidAPIKey',
        "message": "Invalid API Key"
    }

    RequiredParametersMissing = {
        "code": 400,
        "error_code": 'RequiredParametersMissing',
        "message": "Required rarameters are missing: "
    }

    OrderAttributeNotFound = {
        "code": 400,
        "error_code": 'OrderAttributeNotFound',
        "message": "Order attribute is not found. Available options are: "
    }

# Error reason enum

class ErrorReason(enum.Enum):
    NoReason = 0
    RequiredParametersMissing = 1
    OrderAttributeNotFound = 2

