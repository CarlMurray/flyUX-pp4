from django.shortcuts import render, redirect
from .models import Flight, Airport, Passenger, Booking
from datetime import datetime, timedelta
from datetime import date as d
from utils.altdates import create_alt_date_range
from .forms import PassengerForm
from django.http import HttpResponse
import time
from django.core.exceptions import BadRequest, PermissionDenied
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home_page(request):
    """
    Summary:
        Renders the home page.

    Context:
        airports: All airports in the database to show in search form.

    Returns:
        render: Rendered home page.
    """
    airports = Airport.objects.all()
    return render(request, "core/index.html", {"airports": airports})


def search_results_view(request):
    """
    Summary:
        Renders the search results page with flight results based on the search form.

    Context:
        trip_type: The type of trip (one-way or return).
        origin: The origin airport.
        destination: The destination airport.
        outbound_date: The outbound date.
        return_date: The return date.
        flight_results: The flight results based on the search form.
        slider_date_list: The list of dates to show in the date slider.
        passengers: The number of passengers.

    Returns:
        render: Rendered search results page.

    """
    max_date = datetime(2024, 7, 1)
    min_date = datetime.today() - timedelta(days=1)

    # FOR ONE-WAY FLIGHTS
    request.session["num_passengers"] = int(request.GET["passengers"])
    request.session["trip_type"] = request.GET["trip_type"]
    trip_type = request.GET["trip_type"]
    origin = request.GET["origin"][-4:-1]  # GETS IATA CODE
    destination = request.GET["destination"][-4:-1]  # GETS IATA CODE
    outbound_date = request.GET["outbound_date"]
    request.session["outbound_date"] = outbound_date
    # STORES PREVIOUS DATE FOR ALT DATE VALIDATION
    request.session["outbound_previous_date"] = outbound_date
    passengers = request.GET["passengers"]
    #  GETS FLIGHT RESULTS
    flight_origin = Airport.objects.filter(iata=origin.upper()).get()
    flight_destination = Airport.objects.filter(iata=destination.upper()).get()
    flight_results = Flight.objects.filter(
        origin=flight_origin,
        destination=flight_destination,
        outbound_date=outbound_date,
    )
    #  IF TRIP TYPE IS RETURN, GET RETURN FLIGHT RESULTS
    if trip_type == "return":
        return_date = request.GET["return_date"]
        request.session["return_date"] = return_date
        # STORES PREVIOUS DATE FOR ALT DATE VALIDATION
        request.session["return_previous_date"] = return_date
        #  GETS RETURN FLIGHT RESULTS
        flight_results_return = Flight.objects.filter(
            origin=flight_destination,
            destination=flight_origin,
            outbound_date=return_date,
        )
        # CONTEXT FOR RETURN TRIP
        context = {
            "trip_type": trip_type,
            "origin": request.GET["origin"],
            "destination": request.GET["destination"],
            "outbound_date": datetime.strptime(outbound_date, "%Y-%m-%d"),
            "return_date": datetime.strptime(return_date, "%Y-%m-%d"),
            "flight_results": flight_results,
            "slider_date_list": create_alt_date_range(outbound_date),
            "slider_date_list_return": create_alt_date_range(return_date),
            "flight_results_return": flight_results_return,
            "max_date": max_date,
            "min_date": min_date,
        }
    # CONTEXT FOR ONE-WAY TRIP
    else:
        context = {
            "trip_type": trip_type,
            "origin": request.GET["origin"],
            "destination": request.GET["destination"],
            "outbound_date": datetime.strptime(outbound_date, "%Y-%m-%d"),
            "flight_results": flight_results,
            "slider_date_list": create_alt_date_range(outbound_date),
            "max_date": max_date,
            "min_date": min_date,
        }
    return render(request, "core/search-results.html", context)


def passenger_details_view(request):
    """
    Summary:
        Renders the passenger details page.

    Context:
        passengers: The number of passengers.
        passengers_range: Number of form fields to show based on number of passengers.

    Returns:
        GET: Rendered passenger details page.
        POST: Redirects to checkout page.
    """

    #  RENDERS PAGE WITH PASSENGER FORMS
    if request.method == "GET":
        request.session["next_url"] = request.get_full_path()
        request.session["outbound_flight"] = request.GET.get("outbound_flight")
        request.session["outbound_fare"] = request.GET.get("outbound_fare")
        request.session["return_flight"] = request.GET.get("return_flight")
        request.session["return_fare"] = request.GET.get("return_fare")
        passengers = request.session["num_passengers"]
        passengers_range = range(1, (int(passengers) + 1))
        #  RAISES BAD REQUEST IF PASSENGERS IS NOT BETWEEN 1 AND 8
        if int(passengers) > 8 or int(passengers) < 1:
            raise BadRequest
        return render(
            request,
            "core/passenger-details.html",
            {"passengers": passengers_range, "num_passengers": passengers},
        )
    # IF POST, VALIDATES PASSENGER FORMS AND REDIRECTS TO CHECKOUT
    else:
        num_passengers = request.POST["number-of-passengers"]
        request.session["num_passengers"] = num_passengers
        passengers = {}
        #  LOOPS THROUGH PASSENGER FORMS AND VALIDATES
        for p in range(1, (int(num_passengers) + 1)):
            first = request.POST[f"passenger-{p}-first"]
            last = request.POST[f"passenger-{p}-last"]
            data = {"first": first, "last": last}
            form = PassengerForm(data)
            if form.is_valid():
                form = form.cleaned_data
                passenger_key = f"passenger-{p}"
                passengers[passenger_key] = form
        request.session["passengers"] = passengers
        request.session["trip_email"] = request.POST.get("trip-email")
        return redirect("checkout")


def alt_dates(request):
    """
    Summary:
        Handles alternate date search requests when user clicks on alternate date.

    Context:
        leg: The leg of the trip (outbound or return).
        date: The date to search for as selected by the user.
        origin: The origin airport IATA as a string.
        destination: The destination airport IATA as a string.
        flight_origin: The origin airport object.
        flight_destination: The destination airport object.
        leg_string: The leg of the trip (outbound or return) as a string for use in messages.
        other_leg: The opposite leg of the trip (outbound or return) as a string for use in messages.
        flight_results: The flight results for the leg.
        flight_results_return: The flight results for the other leg.

    Returns:
        Rendered search results page with new flight results.
    """
    max_date = datetime(2024, 7, 1)
    min_date = datetime.today() - timedelta(days=1)
    # TELLS VIEW WHICH LEG OF THE TRIP TO SEARCH FOR
    leg = request.GET["leg"]
    # USER SELECTED DATE
    date = request.GET["date"]
    #  ORIGIN AND DESTINATION IATA CODES FOR FLIGHT SEARCH
    origin = request.GET["origin"][-4:-1]  # GETS IATA CODE
    destination = request.GET["destination"][-4:-1]  # GETS IATA CODE
    # ORIGIN AND DESTINATION AIRPORT OBJECTS FOR FLIGHT SEARCH
    flight_origin = Airport.objects.filter(iata=origin.upper()).get()
    flight_destination = Airport.objects.filter(iata=destination.upper()).get()
    # STORES DATE IN SESSION FOR VALIDATION
    request.session[f"{leg}_date"] = request.GET["date"]
    # IF RETURN TRIP
    if request.session["trip_type"] == "return":
        # CHECKS IF RETURN DATE IS BEFORE OUTBOUND DATE
        # IF SO, RAISES ERROR AND RETURNS SAME FLIGHT RESULTS
        if datetime.strptime(
            request.session["outbound_date"], "%Y-%m-%d"
        ) >= datetime.strptime(request.session["return_date"], "%Y-%m-%d"):
            # DEFINES STRINGS FOR MESSAGE
            if leg == "outbound":
                leg_string = "Outbound"
                other_leg = "return"
                tense_string = "before"
            else:
                leg_string = "Return"
                other_leg = "outbound"
                tense_string = "after"
            # MESSAGE IF RETURN DATE IS BEFORE OUTBOUND DATE
            messages.error(
                request,
                f"{leg_string} flight date must be {tense_string} {other_leg} date",
            )
            # STORES PREVIOUS DATE FOR VALIDATION
            request.session[f"{leg}_date"] = request.session[f"{leg}_previous_date"]
            date = request.session[f"{leg}_previous_date"]
            # GETS FLIGHT RESULTS FOR PREVIOUS DATE IF RETURN DATE SELECTED IS BEFORE OUTBOUND DATE
            flight_results = Flight.objects.filter(
                origin=flight_origin, destination=flight_destination, outbound_date=date
            )
            # DEFINES DATES TO SHOW IN SLIDER
            slider_date_list = create_alt_date_range(date)
            context = {
                "flight_results": flight_results,
                "slider_date_list": slider_date_list,
                "date": datetime.strptime(date, "%Y-%m-%d"),
                "origin": flight_origin,
                "destination": flight_destination,
                "leg": leg,
                "max_date": max_date,
                "min_date": min_date,
            }

            return render(request, "partials/flights.html", context)

    # IF DATE IS VALID, GETS FLIGHT RESULTS FOR DATE
    flight_results = Flight.objects.filter(
        origin=flight_origin, destination=flight_destination, outbound_date=date
    )
    slider_date_list = create_alt_date_range(date)
    context = {
        "flight_results": flight_results,
        "slider_date_list": slider_date_list,
        "date": datetime.strptime(date, "%Y-%m-%d"),
        "origin": flight_origin,
        "destination": flight_destination,
        "leg": leg,
        "max_date": max_date,
        "min_date": min_date,
    }
    # ARTIFICIAL LOADING DELAY FOR VISUAL CONSISTENCY
    time.sleep(0.5)
    # STORES PREVIOUS DATE FOR VALIDATION
    request.session[f"{leg}_previous_date"] = date
    return render(request, "partials/flights.html", context)


@login_required
def checkout_view(request):
    """
    Summary:
        Handles checkout requests using selected flights and fares.

    Context:
        passengers: The passengers on the trip.
        outbound_flight: The outbound flight number.
        outbound_fare: The outbound fare code.
        outbound_price: The price of the outbound flight.
        return_flight: The return flight number.
        return_fare: The return fare code.
        return_price: The price of the return flight.
        total_price: The total price of the trip.

    Returns:
        GET: Rendered checkout page.
        POST: Redirect to payment page.

    """
    # DEFINES DATA FOR CONTEXT REGARDLESS OF REQUEST METHOD
    # GETS PASSENGER INFO FROM SESSION
    passengers = request.session["passengers"]
    # USES STORED FLIGHT NUMBERS AND FARES TO GET FLIGHT OBJECTS AND PRICES
    outbound_flight = Flight.objects.get(
        flight_number=request.session["outbound_flight"]
    )
    outbound_fare = request.session["outbound_fare"]
    outbound_price = outbound_flight.get_fare(outbound_fare)
    request.session["outbound_flight_object"] = outbound_flight.id
    # MULTIPLIES PRICE BY NUMBER OF PASSENGERS TO GET TOTAL PRICE
    total_price = int(request.session["num_passengers"]) * outbound_price
    # IF RETURN TRIP, GETS RETURN FLIGHT INFO
    if request.session["trip_type"] == "return":
        # USES STORED FLIGHT NUMBERS AND FARES TO GET FLIGHT OBJECTS AND PRICES
        return_flight = Flight.objects.get(
            flight_number=request.session["return_flight"]
        )
        return_fare = request.session["return_fare"]
        return_price = return_flight.get_fare(return_fare)
        total_price = (
            int(request.session["num_passengers"]) * outbound_price
            + int(request.session["num_passengers"]) * return_price
        )
        # STORE FLIGHT INFO IN SESSIONS FOR REUSE IN BOOKING CREATION
        request.session["return_flight_object"] = return_flight.id
        context = {
            "passengers": passengers,
            "outbound_flight": outbound_flight,
            "outbound_fare": outbound_fare,
            "return_flight": return_flight,
            "return_fare": return_fare,
            "outbound_price": outbound_price,
            "return_price": return_price,
            "total_price": total_price,
            "flights": (
                (outbound_flight, outbound_fare, outbound_price),
                (return_flight, return_fare, return_price),
            ),
            "num_passengers": request.session["num_passengers"],
        }
    # IF ONE WAY TRIP
    else:
        context = {
            "passengers": passengers,
            "outbound_flight": outbound_flight,
            "outbound_fare": outbound_fare,
            "outbound_price": outbound_price,
            "total_price": total_price,
            "flights": [(outbound_flight, outbound_fare, outbound_price)],
            "num_passengers": request.session["num_passengers"],
        }
    # IF GET REQUEST, RENDER CHECKOUT PAGE
    if request.method == "GET":
        return render(request, "core/checkout.html", context)
    # IF PAYMENT FORM SUBMITTED CREATE BOOKING AND PASSENGER OBJs
    elif request.method == "POST":
        #  IF RETURN TRIP, CREATE BOOKING WITH RETURN FLIGHT
        if request.session["trip_type"] == "return":
            booking = Booking(
                outbound_flight_id=request.session["outbound_flight_object"],
                return_flight_id=request.session["return_flight_object"],
                customer=request.user,
                trip_email=request.session["trip_email"],
                status_confirmed=True,
            )
        #  IF ONE WAY TRIP, CREATE BOOKING WITHOUT RETURN FLIGHT
        else:
            booking = Booking(
                outbound_flight_id=request.session["outbound_flight_object"],
                customer=request.user,
                trip_email=request.session["trip_email"],
                status_confirmed=True,
            )
        booking.save()
        #  CREATE PASSENGER OBJECTS FOR EACH PASSENGER
        passengers = request.session["passengers"].items()
        passenger_objects = []
        for passenger, name in passengers:
            p = Passenger(first=name["first"],
                          last=name["last"], booking=booking)
            passenger_objects.append(p)
            p.save()

        return redirect("order-confirmation", id=booking.id)


@login_required
def order_confirmation_view(request, id):
    """
    Summary:
        Renders order confirmation page for a given booking.
    """
    booking = Booking.objects.get(id=id)
    context = {"booking": booking}
    # CHECK THAT USER IS AUTHORISED TO VIEW BOOKING
    if booking.customer != request.user:
        raise PermissionDenied
    return render(request, "core/order-confirmation.html", context)


@login_required
def bookings_view(request):
    """
    Summary:
        Renders bookings page for a given user.
    """
    bookings = Booking.objects.select_related(
        'outbound_flight__origin',
        'return_flight__origin',
        'return_flight__destination',
        'outbound_flight__destination',
        'outbound_flight',
        'return_flight'
    ).filter(customer=request.user)
    context = {"bookings": bookings}
    return render(request, "core/bookings.html", context)


@login_required
def bookings_detail_view(request, booking_id):
    """
    Summary:
        Renders booking detail page for a given booking.

    Returns:
        GET: Rendered booking detail page.
        DELETE: Cancel booking and redirect to bookings page.

    """
    booking = Booking.objects.select_related(
        'customer',
        'outbound_flight__origin',
        'return_flight__origin',
        'return_flight__destination',
        'outbound_flight__destination',
        'outbound_flight',
        'return_flight'
    ).get(id=booking_id)
    # CHECK THAT USER IS AUTHORISED TO VIEW BOOKING
    if request.user != booking.customer:
        raise PermissionDenied
    #  IF DELETE REQUEST, CANCEL BOOKING AND REDIRECT TO BOOKINGS PAGE
    if request.method == "DELETE":
        booking.delete()
        response = HttpResponse()
        messages.success(
            request,
            "You cancelled a booking. Keep an eye on your account for your refund!",
        )
        response.headers["HX-Redirect"] = "/bookings/"
        return response
    #  IF GET REQUEST, RENDER BOOKING DETAIL PAGE
    passengers = Passenger.objects.filter(booking=booking)
    context = {"booking": booking, "passengers": passengers}
    return render(request, "core/bookings-detail.html", context)


@login_required
def bookings_edit_view(request, booking_id):
    """
    Summary:
        Handles htmx requests to edit passenger info for a given booking.

    Returns:
        GET: Rendered edit passenger info form.
        POST: Save edited passenger info and return updated passenger info.
        DELETE: Cancel editing and return original passenger info.
    """
    # GET THE BOOKING OBJ AND ASSOCIATED PASSENGERS
    booking = Booking.objects.get(id=booking_id)
    passengers = Passenger.objects.filter(booking=booking)
    # SAVES EDITED PASSENGER INFO IF 'POST' REQUEST
    if request.method == "POST":
        for passenger in passengers:
            passenger.first = request.POST.get(f"first-{passenger.id}")
            passenger.last = request.POST.get(f"last-{passenger.id}")
            passenger.save()
        messages.success(request, "Passenger info updated!")
    # 'GET' AND 'DELETE' REQUESTS USE SAME CONTEXT DATA
    return render(
        request,
        "partials/passengers-edit.html",
        {"passengers": passengers, "booking": booking},
    )


def about_view(request):
    """
    Summary: Renders about page.
    """
    return render(request, "base/about.html")
