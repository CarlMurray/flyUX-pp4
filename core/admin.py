from django.contrib import admin
from .models import *

class FlightAdmin(admin.ModelAdmin):
    search_fields=['flight_number']

class BookingAdmin(admin.ModelAdmin):
    autocomplete_fields = ['outbound_flight', 'return_flight']

admin.site.register(Airport)
admin.site.register(Aircraft)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Passenger)