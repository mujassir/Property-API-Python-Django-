from propertyapp.common.constants import Constants
from django.db import models
from django.db.models import F, Func

# Implemented Haversine Formula to calculate distances based on Latitude and Longitude.

# https://gist.github.com/rchrd2/5e0b014640a459a14ef038975d2a3683

# This class creates query filters to calculate distances in the db

class DistanceManager(models.Manager):
    def get_with_distance(self, latitude, longitude):
        """
        Returns a QuerySet of locations annotated with their distance from the
        given point. This can then be filtered.
        Usage:
            Foo.objects.within(lat, lon).filter(distance__lt=10).count()
        @see http://stackoverflow.com/a/31715920/1373318
        """
        class Sin(Func):
            function = 'SIN'
        class Cos(Func):
            function = 'COS'
        class Acos(Func):
            function = 'ACOS'
        class Radians(Func):
            function = 'RADIANS'

        radlat = Radians(latitude) # given latitude
        radlong = Radians(longitude) # given longitude
        radflat = Radians(F('latitude'))
        radflong = Radians(F('longitude'))

        # Note 3959.0 is for miles. Use 6371 for kilometers
        Expression = Constants.EARCH_RADIUS_KM * Acos(Cos(radlat) * Cos(radflat) *
                                   Cos(radflong - radlong) +
                                   Sin(radlat) * Sin(radflat))

        return self.get_queryset()\
            .exclude(latitude=None)\
            .exclude(longitude=None)\
            .annotate(distance=Expression)

            