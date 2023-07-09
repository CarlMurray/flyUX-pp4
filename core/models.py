from django.db import models
from django.core.validators import RegexValidator

flight_number_validator = RegexValidator(regex=r'UX[0-9]+', message='Flight number must be in the format UX000')
iata_validator = RegexValidator(regex=r'[A-Z]+', message='IATA code should be three uppercase letters')

class Airport(models.Model):
    name = models.CharField(max_length=50, verbose_name='Airport name')
    iata = models.CharField(max_length=3, validators=[iata_validator], verbose_name='IATA code')
    locality = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    
class Flight(models.Model):
    flight_number = models.CharField(max_length=50, validators=[flight_number_validator])
    origin = models.ForeignKey("Airport", on_delete=models.CASCADE, related_name='origin')
    destination = models.ForeignKey("Airport", on_delete=models.CASCADE, related_name='destination')
    dep_time = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='Departure time')
    arr_time = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='Arrival time')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    aircraft = models.ForeignKey("Aircraft", on_delete=models.CASCADE, related_name='aircraft')
    
class Aircraft(models.Model):
    
    AIRCRAFT_TYPES = [
        ('b737-700','B737-700'),
        ('b737-600','B737-600'),
        ('a321-100','A321-100'),
        ('a321-200','A321-200')
    ]
    
    identification = models.CharField(max_length=50)
    seats = models.PositiveIntegerField()
    aircraft_type = models.CharField(max_length=50, verbose_name='Aircraft type', choices=AIRCRAFT_TYPES )

