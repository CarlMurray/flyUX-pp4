from django.db import models

class Airport(models.Model):
    name = models.CharField(max_length=50)
    iata = models.CharField(max_length=3)
    locality = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    
class Flight(models.Model):
    flight_number = models.CharField(max_length=50)
    origin = models.ForeignKey("Airport", on_delete=models.CASCADE, related_name='origin')
    destination = models.ForeignKey("Airport", on_delete=models.CASCADE, related_name='destination')
    dep_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    arr_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    aircraft = models.ForeignKey("Aircraft", on_delete=models.CASCADE, related_name='aircraft')
    
class Aircraft(models.Model):
    identification = models.CharField(max_length=50)
    seats = models.PositiveIntegerField()
    ac_type = models.CharField(max_length=50)
