from django.shortcuts import render, redirect
from .models import Flight, Airport

def home_page(request):
    airports = Airport.objects.all()
    return render(request, 'core/index.html', {'airports':airports})

def search_results_view(request):
    trip_type = request.GET['trip_type']
    origin = request.GET['origin'][-4:-1] # GETS IATA CODE
    destination = request.GET['destination'][-4:-1] # GETS IATA CODE
    outbound_date = request.GET['outbound_date']
    return_date = request.GET['return_date']
    flight_origin = Airport.objects.filter(iata=origin.upper()).get()
    flight_destination = Airport.objects.filter(iata=destination.upper()).get()
    flight_results = Flight.objects.filter(
        origin=flight_origin,
        destination=flight_destination,        
        outbound_date=outbound_date
        )
    print(flight_results)
    context = {
        'flight_results':flight_results
    }
    return render(request, 'core/search-results.html', context)