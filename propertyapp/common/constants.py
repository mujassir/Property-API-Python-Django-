from django.db import models

# Constants to be used in the application


class Constants(models.Model):
    METER = "Meter"
    KILO_Meter = "Kilo Meter"
    MILE = "Mile"
    # Note 3959.0 is for miles. Use 6371 for kilometers
    EARCH_RADIUS_KM = 6371
    EARCH_RADIUS_MILES = 3959
