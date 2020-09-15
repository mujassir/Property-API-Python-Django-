from propertyapp.constants import Constants
from django.http import request
from propertyapp.serializer import propertySerializer
from propertyapp.models import propertyModel

# Manager class to apply filters, serialize result set and return

class propertyManager:
    def getProperties(params):

        latitude = params.latitude
        longitude = params.longitude
        distance = params.distance

        querySet = propertyModel.objects2.get_with_distance(
            latitude=latitude, longitude=longitude)

        # distance filter
        querySet = querySet.filter(distance__gt=5, distance__lt=distance)

        # ad_operation filter
        if params.ad_operation != 0:
            querySet = querySet.filter(ad_operation=params.ad_operation)

        # ad_typology filter
        if params.ad_typology != 0:
            querySet = querySet.filter(ad_typology=params.ad_typology)

        # ad_owner_type filter
        if params.ad_owner_type != 0:
            querySet = querySet.filter(ad_owner_type=params.ad_owner_type)

        # minPrice filter
        if not (params.minPrice is None):
            querySet = querySet.filter(price__gte=params.minPrice)

         # maxPrice filter
        if not (params.maxPrice is None):
            querySet = querySet.filter(price__lte=params.maxPrice)

        # order by
        if not (params.order is None):
            order = params.order
            if order == Constants.ORDER_OPTION_ROOM:
                order = Constants.ORDER_OPTION_ROOM_COLUMN_NAME
            if params.sort == "desc":
                order = "-" + order

            querySet = querySet.order_by(order)

        # Distinct and Max records

        querySet = querySet.distinct()[:Constants.MAX_RECORD_COUNT]

        serializer = propertySerializer(querySet, many=True, context={
            'longitude': longitude, 'latitude': latitude, 'distance': distance})
        return serializer.data
