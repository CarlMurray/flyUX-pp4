from django.shortcuts import render, redirect
from .models import Flight, Airport
from datetime import datetime, timedelta

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
    sorted_price = flight_results.values_list('price')
    lowest_price = float(sorted_price.order_by('price').first()[0])
    slider_date_list = [] 
    slider_date_range = range(-2, 3)
    for x in slider_date_range:
        date = datetime.strptime(outbound_date, '%Y-%m-%d') + timedelta(days=x)
        slider_date_list.append(date)
    print(slider_date_list)
    
    context = {
        'origin':request.GET['origin'],
        'destination':request.GET['destination'],
        'outbound_date':datetime.strptime(outbound_date, '%Y-%m-%d'),
        'lowest_price':lowest_price,
        'flight_results':flight_results,
        'slider_date_list':slider_date_list
    }
    return render(request, 'core/search-results.html', context)