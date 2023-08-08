from django.shortcuts import render, redirect
from .models import Flight, Airport, Passenger, Booking
from datetime import datetime, timedelta
from utils.altdates import create_alt_date_range
from .forms import PassengerForm
from django.http import HttpResponse

def home_page(request):
    airports = Airport.objects.all()
    return render(request, 'core/index.html', {'airports': airports})


def search_results_view(request):
    request.session['num_passengers'] = int(request.GET['passengers'])
    trip_type = request.GET['trip_type']
    origin = request.GET['origin'][-4:-1]  # GETS IATA CODE
    destination = request.GET['destination'][-4:-1]  # GETS IATA CODE
    outbound_date = request.GET['outbound_date']
    return_date = request.GET['return_date']
    passengers = request.GET['passengers']
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
        'trip_type': trip_type,
        'origin': request.GET['origin'],
        'destination': request.GET['destination'],
        'outbound_date': datetime.strptime(outbound_date, '%Y-%m-%d'),
        'return_date': datetime.strptime(return_date, '%Y-%m-%d'),
        # 'lowest_price':lowest_price,
        'flight_results': flight_results,
        'slider_date_list': create_alt_date_range(outbound_date),
        'slider_date_list_return': create_alt_date_range(return_date),
        'flight_results_return': flight_results_return,
    }
    return render(request, 'core/search-results.html', context)


def passenger_details_view(request):
    if request.method == 'GET':
        request.session['outbound_flight'] = request.GET['outbound_flight']
        request.session['outbound_fare'] = request.GET['outbound_fare']
        request.session['return_flight'] = request.GET['return_flight']
        request.session['return_fare'] = request.GET['return_fare']
        # print(dict(request.session))
        # print(request.session['passengers'])
        passengers = int(request.session['num_passengers'])
        passengers_range = range(1, passengers+1)
        # print(passengers_range)
        return render(request, 'core/passenger-details.html', {'passengers': passengers_range, 'num_passengers':passengers})
    else:
        num_passengers = request.POST['number-of-passengers']
        request.session['num_passengers'] = num_passengers
        passengers = {}
        for p in range(1, int(num_passengers)+1):            
            first = request.POST[f'passenger-{p}-first']
            last = request.POST[f'passenger-{p}-last']
            data = {'first':first, 'last':last}
            form = PassengerForm(data)
            print(form)
            if form.is_valid():
                form = form.cleaned_data
                print(str(form))
                passenger_key = f'passenger-{p}'
                passengers[passenger_key] = form
        # print(passengers)
        request.session['passengers'] = passengers
        request.session['trip_email'] = request.POST['trip-email']
        print(dict(request.session))
        return redirect('checkout')
            
            

def alt_dates(request):
    leg = request.GET['leg']
    date = request.GET['date']
    origin = request.GET['origin'][-4:-1]  # GETS IATA CODE
    destination = request.GET['destination'][-4:-1]  # GETS IATA CODE
    flight_origin = Airport.objects.filter(iata=origin.upper()).get()
    flight_destination = Airport.objects.filter(iata=destination.upper()).get()

    flight_results = Flight.objects.filter(
        origin=flight_origin,
        destination=flight_destination,
        outbound_date=date
    )
    # print(f'THIS IS THE SELECTED DATE: {date}')
    # print(type(date))
    slider_date_list = create_alt_date_range(date)
    # print(slider_date_list)
    context = {
        'flight_results': flight_results,
        'slider_date_list': slider_date_list,
        'date': datetime.strptime(date, '%Y-%m-%d'),
        'origin': flight_origin,
        'destination': flight_destination,
        'leg': leg
    }
    return render(request, 'partials/flights.html', context)


def checkout_view(request):
    passengers = request.session['passengers']
    outbound_flight = Flight.objects.get(flight_number=request.session['outbound_flight'])
    print(outbound_flight)
    outbound_fare = request.session['outbound_fare']
    outbound_price = outbound_flight.get_fare(outbound_fare)
    return_flight = Flight.objects.get(flight_number=request.session['return_flight'])
    return_fare = request.session['return_fare']
    return_price = return_flight.get_fare(return_fare)
    total_price = int(request.session['num_passengers']) * outbound_price + int(request.session['num_passengers']) * return_price
    request.session['outbound_flight_object'] = outbound_flight.id
    request.session['return_flight_object'] = return_flight.id
    
    context = {
        'passengers':passengers,
        'outbound_flight':outbound_flight,
        'outbound_fare':outbound_fare,
        'return_flight':return_flight,
        'return_fare':return_fare,
        'outbound_price':outbound_price,
        'return_price':return_price,
        'total_price':total_price,
        'flights':((outbound_flight, outbound_fare, outbound_price), (return_flight, return_fare, return_price)),
        'num_passengers':request.session['num_passengers']
    }
    # STORE FLIGHT INFO IN SESSIONS FOR REUSE IN OTHER VIEWS
    # request.session['booking_info'] = context
    if request.method == 'GET':
        return render(request, 'core/checkout.html', context)
    return redirect('order-confirmation')


def order_confirmation_view(request):
    request.session['outbound_flight_object']
    request.session['return_flight_object']

    booking = Booking(
        outbound_flight_id=request.session['outbound_flight_object'], 
        return_flight_id=request.session['return_flight_object'],
        customer=request.user,
        trip_email = request.session['trip_email'],
        status_confirmed = True,
        )
    booking.save()
    print(request.session['passengers'])
    passengers = request.session['passengers'].items()
    passenger_objects = []
    for passenger, name in passengers:
        print(passenger, name)
        p = Passenger(first=name['first'], last=name['last'], booking=booking)
        passenger_objects.append(p)
        p.save()

    context = {}
    return render(request, 'core/order-confirmation.html', context)


def bookings_view(request):
    bookings = Booking.objects.filter(customer=request.user)
    context={'bookings':bookings}
    return render(request, 'core/bookings.html', context)

def bookings_detail_view(request, booking_id):
        
    booking = Booking.objects.get(id=booking_id)
    if request.method == "DELETE":
        booking.delete()
        response = HttpResponse()
        response.headers['HX-Redirect'] = "/bookings/"
        return response
    passengers = Passenger.objects.filter(booking=booking)
    print(passengers)
    context={
        'booking':booking,
        'passengers':passengers
    }
    return render(request, 'core/bookings-detail.html', context)

def bookings_edit_view(request, booking_id):
    # GET THE BOOKING OBJ AND ASSOCIATED PASSENGERS
    booking = Booking.objects.get(id=booking_id)
    passengers = Passenger.objects.filter(booking=booking)
    # SAVES EDITED PASSENGER INFO IF 'POST' REQUEST
    if request.method == "POST":
        for passenger in passengers:
            passenger.first = request.POST[f'first-{passenger.id}']
            passenger.last = request.POST[f'last-{passenger.id}']
            passenger.save()
    # 'GET' AND 'DELETE' REQUESTS USE SAME CONTEXT DATA
    return render(request, 'partials/passengers-edit.html', {'passengers':passengers, 'booking':booking})