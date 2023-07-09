from django.db import models

class Airport(models.Model):
    name = models.CharField(max_length=50)
    iata = models.CharField(max_length=3)
    locality = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    country = models.CharField(max_length=50)