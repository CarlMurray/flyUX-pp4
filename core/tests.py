from django.test import TestCase
from .models import *
from datetime import datetime


class AiportTestCase(TestCase):
    def setUp(self):
        Airport.objects.create(name='Testport', iata='TST',
                               locality='Test', region='Tester', country='Testing')

    def test_airport_str(self):
        a = Airport.objects.get(iata='TST')
        print(a)
        self.assertEqual(str(a), 'Testport (TST)')


class FlightTestCase(TestCase):
    def setUp(self):
        Airport.objects.bulk_create(
            [
                Airport(
                    name='Origin',
                    iata='ORG',
                    locality='Org',
                    region='Ogn',
                    country='Orgtest'
                ),
                Airport(
                    name='Destination',
                    iata='DST',
                    locality='Dest',
                    region='Dst',
                    country='Dsttest'
                ),
            ]
        )
        Aircraft.objects.create(
            identification='TEST123',
            seats=100,
            aircraft_type='b737-700'
        )
        origin = Airport.objects.get(iata='ORG')
        destination = Airport.objects.get(iata='DST')
        aircraft = Aircraft.objects.first()
        Flight.objects.create(
            flight_number='UX00001',
            origin=origin,
            destination=destination,
            outbound_date=datetime.strptime('2023-01-05', '%Y-%m-%d'),
            dep_time=datetime.now(),
            arr_time=datetime.now(),
            price=100,
            aircraft=aircraft
        )

    def test_flight_str(self):
        flight = Flight.objects.get(flight_number='UX00001')
        self.assertEqual(
            str(flight), 'UX00001, Origin (ORG) --> Destination (DST)')

    def test_standard_fare(self):
        flight = Flight.objects.get(flight_number='UX00001')
        self.assertEqual(flight.standard_fare(), flight.price)

    def test_plus_fare(self):
        flight = Flight.objects.get(flight_number='UX00001')
        self.assertEqual(flight.plus_fare(), flight.price+17)

    def test_premium_fare(self):
        flight = Flight.objects.get(flight_number='UX00001')
        self.assertEqual(flight.premium_fare(), flight.price+31)

    def test_get_fare(self):
        flight = Flight.objects.get(flight_number='UX00001')
        self.assertEqual(flight.get_fare('Standard'), flight.price)
        self.assertEqual(flight.get_fare('Plus'), flight.price+17)
        self.assertEqual(flight.get_fare('Premium'), flight.price+31)


class AircraftTestCase(TestCase):
    def setUp(self):
        Aircraft.objects.create(
            identification='TEST123',
            seats=100,
            aircraft_type=Aircraft.AIRCRAFT_TYPES[0][1]
        )

    def test_aircraft_str(self):
        aircraft = Aircraft.objects.first()
        self.assertEqual(str(aircraft), aircraft.get_aircraft_type_display())


class PassengerTestCase(TestCase):
    def test_passenger_str(self):
        passenger = Passenger(first='Test', last='McTesterson')
        self.assertEqual(str(passenger), 'Test McTesterson')


class BookingTestCase(TestCase):
    def setUp(self):
        Airport.objects.bulk_create(
            [
                Airport(
                    name='Origin',
                    iata='ORG',
                    locality='Org',
                    region='Ogn',
                    country='Orgtest'
                ),
                Airport(
                    name='Destination',
                    iata='DST',
                    locality='Dest',
                    region='Dst',
                    country='Dsttest'
                ),
            ]
        )
        Aircraft.objects.create(
            identification='TEST123',
            seats=100,
            aircraft_type=Aircraft.AIRCRAFT_TYPES[0][1]
        )
        Flight.objects.create(
            flight_number='UX00001',
            origin=Airport.objects.get(iata='ORG'),
            destination=Airport.objects.get(iata='DST'),
            outbound_date=datetime.strptime('2023-01-05', '%Y-%m-%d'),
            dep_time=datetime.now(),
            arr_time=datetime.now(),
            price=100,
            aircraft=Aircraft.objects.first()
        )
        Flight.objects.create(
            flight_number='UX00002',
            origin=Airport.objects.get(iata='DST'),
            destination=Airport.objects.get(iata='ORG'),
            outbound_date=datetime.strptime('2023-01-05', '%Y-%m-%d'),
            dep_time=datetime.now(),
            arr_time=datetime.now(),
            price=100,
            aircraft=Aircraft.objects.first()
        )
        Booking.objects.create(
            reference='52abb40b-7c2d-4d2d-a7b0-589f7687abd1',
            outbound_flight=Flight.objects.get(flight_number='UX00001'),
            return_flight=Flight.objects.get(flight_number='UX00002'),
            customer=User.objects.create(email='test@text.com',
                                         first_name='Test', last_name='McTesterson'),
        )

    def test_booking_str(self):
        booking = Booking.objects.first()
        self.assertEqual(str(
            booking), 'Reference: 52ABB40B; Origin (ORG) - Destination (DST); Test McTesterson')

    def test_get_shorthand(self):
        booking = Booking.objects.first()
        self.assertEqual(booking.get_shorthand(), '52ABB40B')
