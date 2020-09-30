from django.http import JsonResponse
from propertyapp.config.configuration import Configuration
from propertyapp.config.error_message import ErrorMessage
from propertyapp.config.error_reason import ErrorReason
from propertyapp.api_key_validator import APIKeyValidator
from propertyapp.common.property_manager import PropertyManager
from propertyapp.models import PropertyInputModel
from rest_framework.response import Response
from rest_framework.decorators import api_view
import copy

# POST method implementation for property API

@api_view(['POST'])
def propertyAPI(request):
    if request.method == 'POST':

        # Get post parameters
        params = PropertyInputModel.create(request.data)

        # Validate required parameters
        if params.is_valid == False:
            if params.error_reason == ErrorReason.RequiredParametersMissing:
                message = copy.deepcopy(
                    ErrorMessage.RequiredParametersMissing)
                message["message"] += params.missing_parameters
                return JsonResponse(message)
            if params.error_reason == ErrorReason.OrderAttributeNotFound:
                message = copy.deepcopy(ErrorMessage.OrderAttributeNotFound)
                message["message"] += ",".join(Configuration.ORDER_OPTIONS)
                return JsonResponse(message)

        # Validate APIKEY

        if APIKeyValidator.Validate(params.APIKEY) == False:
            return JsonResponse(Configuration.InvalidAPIKey)

        response = PropertyManager.getProperties(params)
        return Response(response)
