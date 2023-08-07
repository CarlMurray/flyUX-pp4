from django.db import models
from django.core.validators import RegexValidator
from users.models import User
import uuid

flight_number_validator = RegexValidator(regex=r'UX\d\d\d\d\d', message='Flight number must be in the format UX00000')
iata_validator = RegexValidator(regex=r'[A-Z]+', message='IATA code should be three uppercase letters')

class Airport(models.Model):
    name = models.CharField(max_length=50, verbose_name='Airport name')
    iata = models.CharField(max_length=3, validators=[iata_validator], verbose_name='IATA code', unique=True)
    locality = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.name} ({self.iata})'
        
class Flight(models.Model):
    flight_number = models.CharField(max_length=50, validators=[flight_number_validator])
    origin = models.ForeignKey("Airport", on_delete=models.CASCADE, related_name='origin')
    destination = models.ForeignKey("Airport", on_delete=models.CASCADE, related_name='destination')
    outbound_date = models.DateField(auto_now=False, auto_now_add=False)
    dep_time = models.TimeField(auto_now=False, auto_now_add=False, verbose_name='Departure time')
    arr_time = models.TimeField(auto_now=False, auto_now_add=False, verbose_name='Arrival time')
    price = models.DecimalField(max_digits=7, decimal_places=0)
    aircraft = models.ForeignKey("Aircraft", on_delete=models.CASCADE, related_name='aircraft')
    
    def __str__(self):
        return f'{self.flight_number}, {self.origin} --> {self.destination}'
    
    def standard_fare(self):
        return self.price
    
    def plus_fare(self):
        return self.price + 17
    
    def premium_fare(self):
        return self.price + 31
    
    def get_fare(self, fare):
        if fare == 'Standard':
            return self.price
        if fare == 'Plus':
            return self.price + 17
        if fare == 'Premium':
            return self.price + 31
    
    
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
    
    def __str__(self):
        return f'{self.aircraft_type}'
    
class Passenger(models.Model):
    booking = models.ForeignKey("Booking", null=True, blank=True, on_delete=models.CASCADE)
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first} {self.last}'

class Booking(models.Model):
    reference = models.UUIDField(default=uuid.uuid4)
    time_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    outbound_flight = models.ForeignKey("Flight", on_delete=models.SET_NULL, null=True, blank=True, related_name="booking_outbound")
    return_flight = models.ForeignKey("Flight", on_delete=models.SET_NULL, null=True, blank=True, related_name="booking_return")
    customer = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True, blank=True)
    status_confirmed = models.BooleanField(blank=True, default=False)
    trip_email = models.EmailField(max_length=254, blank=True, null=True)

    def __str__(self):
        return f'Reference: {self.reference.hex[:10]}; {self.outbound_flight.origin} - {self.outbound_flight.destination}; {self.customer}'
    
    def get_shorthand(self):
        return str(self.reference)[:8].upper()