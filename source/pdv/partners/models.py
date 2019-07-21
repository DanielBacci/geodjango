from django.contrib.gis.db import models


class Partner(models.Model):

    trading_name = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    document = models.CharField(
        max_length=20,
        unique=True
    )
    address = models.PointField()
    coverage_area = models.MultiPolygonField()
