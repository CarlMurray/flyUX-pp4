from django.shortcuts import render, redirect
from .models import Flight, Airport

def home_page(request):
    airports = Airport.objects.all()
    return render(request, 'core/index.html', {'airports':airports})

def search_results_view(request):
    trip_type = request.GET['trip_type']
    origin = request.GET['origin'][-4:-1] # GETS IATA CODE
    destination = request.GET['destination'][-4:-1] # GETS IATA CODE
    date_outbound = request.GET['date_outbound']
    date_return = request.GET['date_return']
    flight_origin = Airport.objects.filter(iata=origin.upper()).get()
    print(flight_origin)
    flight_results = Flight.objects.filter(origin=flight_origin)
    context = {
        'trip_type':trip_type,
        'origin':origin,
        'destination':destination,
        'date_outbound':date_outbound,
        'date_return':date_return,
        'flight_origin':flight_origin,
        'flight_results':flight_results
    }
    return render(request, 'core/search-results.html', context)