from django.shortcuts import render, redirect
from .models import Flight, Airport
from datetime import datetime, timedelta
from utils.altdates import create_alt_date_range

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
    flight_results_return = Flight.objects.filter(
        origin=flight_destination,
        destination=flight_origin,        
        outbound_date=return_date
        )
    # sorted_price = flight_results.values_list('price')
    # lowest_price = float(sorted_price.order_by('price').first()[0])
    
    context = {
        'trip_type':trip_type,
        'origin':request.GET['origin'],
        'destination':request.GET['destination'],
        'outbound_date':datetime.strptime(outbound_date, '%Y-%m-%d'),
        'return_date':datetime.strptime(return_date, '%Y-%m-%d'),
        # 'lowest_price':lowest_price,
        'flight_results':flight_results,
        'slider_date_list':create_alt_date_range(outbound_date),
        'slider_date_list_return':create_alt_date_range(return_date),
        'flight_results_return':flight_results_return,
    }
    return render(request, 'core/search-results.html', context)


def passenger_details_view(request):
    return render(request, 'core/passenger-details.html')

def alt_dates(request):
    leg = request.GET['leg']
    date = request.GET['date']
    origin = request.GET['origin'][-4:-1] # GETS IATA CODE
    destination = request.GET['destination'][-4:-1] # GETS IATA CODE
    flight_origin = Airport.objects.filter(iata=origin.upper()).get()
    flight_destination = Airport.objects.filter(iata=destination.upper()).get()

    flight_results = Flight.objects.filter(
    origin=flight_origin,
    destination=flight_destination,        
    outbound_date=date
    )
    print(f'THIS IS THE SELECTED DATE: {date}')
    print(type(date))
    slider_date_list = create_alt_date_range(date)
    # print(slider_date_list)
    context = {
        'flight_results':flight_results, 
        'slider_date_list':slider_date_list, 
        'date':datetime.strptime(date, '%Y-%m-%d'), 
        'origin':flight_origin, 
        'destination':flight_destination, 
        'leg':leg
        }
    return render(request, 'partials/flights.html', context)