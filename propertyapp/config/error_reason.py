import enum
from django.db import models

# Error reason enum

class ErrorReason(enum.Enum):
    NoReason = 0
    RequiredParametersMissing = 1
    OrderAttributeNotFound = 2

