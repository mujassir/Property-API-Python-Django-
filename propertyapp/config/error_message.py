from django.db import models

# JSON Error messages to be used in the application

class ErrorMessage(models.Model):
    InvalidAPIKey = {
        "code": 401,
        "error_code": 'InvalidAPIKey',
        "message": "Invalid API Key"
    }

    RequiredParametersMissing = {
        "code": 400,
        "error_code": 'RequiredParametersMissing',
        "message": "Required parameters are missing: "
    }

    OrderAttributeNotFound = {
        "code": 400,
        "error_code": 'OrderAttributeNotFound',
        "message": "Order attribute is not found. Available options are: "
    }

