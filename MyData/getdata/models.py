from django.db import models


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100, null=True)
    alpha2code = models.CharField(max_length=100, null=True)
    alpha3code = models.CharField(max_length=100, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)