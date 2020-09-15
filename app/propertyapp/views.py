import decimal
from django.http import JsonResponse
from propertyapp.serializer import propertySerializer
from propertyapp.models import propertyModel
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST'])
def propertyAPI(requst):
    if requst.method == 'POST':
        latitude = requst.data['latitude']
        longitude = requst.data['longitude']
        distance = requst.data['distance']

        querySet = propertyModel.objects2.get_with_distance(latitude=latitude, longitude=longitude).filter(
            distance__gt=5, distance__lt=distance).order_by('distance').distinct()[:100]

        serializer = propertySerializer(querySet, many=True, context={
            'longitude': longitude, 'latitude': latitude, 'distance': distance})
        return Response(serializer.data)

# return JsonResponse({"lat": latitude, "long": longitude, "dist": distance})
