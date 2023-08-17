from django.test import TestCase, Client
from .models import *
from datetime import datetime
from .views import *


class AiportTestCase(TestCase):
    def setUp(self):
        Airport.objects.create(
            name="Testport",
            iata="TST",
            locality="Test",
            region="Tester",
            country="Testing",
        )

    def test_airport_str(self):
        a = Airport.objects.get(iata="TST")
        print(a)
        self.assertEqual(str(a), "Testport (TST)")


class FlightTestCase(TestCase):
    def setUp(self):
        Airport.objects.bulk_create(
            [
                Airport(
                    name="Origin",
                    iata="ORG",
                    locality="Org",
                    region="Ogn",
                    country="Orgtest",
                ),
                Airport(
                    name="Destination",
                    iata="DST",
                    locality="Dest",
                    region="Dst",
                    country="Dsttest",
                ),
            ]
        )
        Aircraft.objects.create(
            identification="TEST123", seats=100, aircraft_type="b737-700"
        )
        origin = Airport.objects.get(iata="ORG")
        destination = Airport.objects.get(iata="DST")
        aircraft = Aircraft.objects.first()
        Flight.objects.create(
            flight_number="UX00001",
            origin=origin,
            destination=destination,
            outbound_date=datetime.strptime("2023-01-05", "%Y-%m-%d"),
            dep_time=datetime.now(),
            arr_time=datetime.now(),
            price=100,
            aircraft=aircraft,
        )

    def test_flight_str(self):
        flight = Flight.objects.get(flight_number="UX00001")
        self.assertEqual(str(flight), "UX00001, Origin (ORG) --> Destination (DST)")

    def test_standard_fare(self):
        flight = Flight.objects.get(flight_number="UX00001")
        self.assertEqual(flight.standard_fare(), flight.price)

    def test_plus_fare(self):
        flight = Flight.objects.get(flight_number="UX00001")
        self.assertEqual(flight.plus_fare(), flight.price + 17)

    def test_premium_fare(self):
        flight = Flight.objects.get(flight_number="UX00001")
        self.assertEqual(flight.premium_fare(), flight.price + 31)

    def test_get_fare(self):
        flight = Flight.objects.get(flight_number="UX00001")
        self.assertEqual(flight.get_fare("Standard"), flight.price)
        self.assertEqual(flight.get_fare("Plus"), flight.price + 17)
        self.assertEqual(flight.get_fare("Premium"), flight.price + 31)


class AircraftTestCase(TestCase):
    def setUp(self):
        Aircraft.objects.create(
            identification="TEST123",
            seats=100,
            aircraft_type=Aircraft.AIRCRAFT_TYPES[0][1],
        )

    def test_aircraft_str(self):
        aircraft = Aircraft.objects.first()
        self.assertEqual(str(aircraft), aircraft.get_aircraft_type_display())


class PassengerTestCase(TestCase):
    def test_passenger_str(self):
        passenger = Passenger(first="Test", last="McTesterson")
        self.assertEqual(str(passenger), "Test McTesterson")


class BookingTestCase(TestCase):
    def setUp(self):
        Airport.objects.bulk_create(
            [
                Airport(
                    name="Origin",
                    iata="ORG",
                    locality="Org",
                    region="Ogn",
                    country="Orgtest",
                ),
                Airport(
                    name="Destination",
                    iata="DST",
                    locality="Dest",
                    region="Dst",
                    country="Dsttest",
                ),
            ]
        )
        Aircraft.objects.create(
            identification="TEST123",
            seats=100,
            aircraft_type=Aircraft.AIRCRAFT_TYPES[0][1],
        )
        Flight.objects.create(
            flight_number="UX00001",
            origin=Airport.objects.get(iata="ORG"),
            destination=Airport.objects.get(iata="DST"),
            outbound_date=datetime.strptime("2023-01-05", "%Y-%m-%d"),
            dep_time=datetime.now(),
            arr_time=datetime.now(),
            price=100,
            aircraft=Aircraft.objects.first(),
        )
        Flight.objects.create(
            flight_number="UX00002",
            origin=Airport.objects.get(iata="DST"),
            destination=Airport.objects.get(iata="ORG"),
            outbound_date=datetime.strptime("2023-01-05", "%Y-%m-%d"),
            dep_time=datetime.now(),
            arr_time=datetime.now(),
            price=100,
            aircraft=Aircraft.objects.first(),
        )
        Booking.objects.create(
            reference="52abb40b-7c2d-4d2d-a7b0-589f7687abd1",
            outbound_flight=Flight.objects.get(flight_number="UX00001"),
            return_flight=Flight.objects.get(flight_number="UX00002"),
            customer=User.objects.create(
                email="test@text.com", first_name="Test", last_name="McTesterson"
            ),
        )

    def test_booking_str(self):
        booking = Booking.objects.first()
        self.assertEqual(
            str(booking),
            "Reference: 52ABB40B; Origin (ORG) - Destination (DST); Test McTesterson",
        )

    def test_get_shorthand(self):
        booking = Booking.objects.first()
        self.assertEqual(booking.get_shorthand(), "52ABB40B")


# -------------------------------------
# VIEWS TESTS
# -------------------------------------


class HomePageViewTestCase(TestCase):
    """
    Test case for testing home_page view.
    """
    def setUp(self):
        """
        Creates Airports for tests.
        Defines Client().
        """
        Airport.objects.bulk_create(
            [
                Airport(
                    name="Origin",
                    iata="ORG",
                    locality="Org",
                    region="Ogn",
                    country="Orgtest",
                ),
                Airport(
                    name="Destination",
                    iata="DST",
                    locality="Dest",
                    region="Dst",
                    country="Dsttest",
                ),
            ]
        )

        self.client = Client()

    def test_home_page_templates(self):
        """
        Tests templates used for home_page view.
        Simulates a request to home_page. 
        Adds each template name to template_list. 
        Compares template_list with template name strings.
        """
        request = self.client.get("")
        template_list = []
        for t in request.templates:
            template_list.append(t.name)
        self.assertListEqual(template_list, ["core/index.html", "base/base.html"])

    def test_home_page_context(self):
        """
        Tests context passed from home_page view to template.
        Asserts that airports Queryset same as context.
        """
        response = self.client.get("")
        airports = Airport.objects.all()
        self.assertQuerysetEqual(response.context["airports"], airports, ordered=False)


class SearchResultsViewTestCase(TestCase):
    """
    Test case for testing search_results view.
    """
    def setUp(self):
        """
        Creates Airports for tests.
        Defines Client().
        """
        self.client = Client()
        Airport.objects.bulk_create(
            [
                Airport(
                    name="Origin",
                    iata="ORG",
                    locality="Org",
                    region="Ogn",
                    country="Orgtest",
                ),
                Airport(
                    name="Destination",
                    iata="DST",
                    locality="Dest",
                    region="Dst",
                    country="Dsttest",
                ),
            ]
        )


    def test_num_passengers(self):
        """
        Tests that num_passengers is an int.
        """
        response = self.client.get('/search_results/', {
            'passengers':'5',
            'trip_type':'return',
            'origin':'(ORG)',
            'destination':'(DST)',
            'outbound_date':'2023-01-10',
            'return_date':'2023-02-10',
            })
        self.assertDictEqual(dict(self.client.session), {'num_passengers': 5, 'trip_type': 'return'})

    def test_oneway_trip(self):
        """
        Tests context for one-way trip option.
        """
        response = self.client.get('/search_results/', {
            'passengers':'5',
            'trip_type':'oneway',
            'origin':'(ORG)',
            'destination':'(DST)',
            'outbound_date':'2023-01-10',
            })
        self.assertDictEqual(dict(self.client.session), {'num_passengers': 5, 'trip_type': 'oneway'})


class PassengerDetailsViewTestCase(TestCase):
    """
    Test case for testing passenger_details view.
    """
    def setUp(self):
        """
        Initiates Client().
        Defines session and adds num_passengers for testing.
        Creates test data from models.
        """
        self.client = Client()
        session = self.client.session
        session['num_passengers'] = 2
        session.save()
        Aircraft.objects.create(
            identification="TEST123",
            seats=100,
            aircraft_type=Aircraft.AIRCRAFT_TYPES[0][1],
        )

        Airport.objects.bulk_create(
            [
                Airport(
                    name="Origin",
                    iata="ORG",
                    locality="Org",
                    region="Ogn",
                    country="Orgtest",
                ),
                Airport(
                    name="Destination",
                    iata="DST",
                    locality="Dest",
                    region="Dst",
                    country="Dsttest",
                ),
            ]
        )

        Flight.objects.create(
            flight_number="UX00001",
            origin=Airport.objects.get(iata="ORG"),
            destination=Airport.objects.get(iata="DST"),
            outbound_date=datetime.strptime("2023-01-05", "%Y-%m-%d"),
            dep_time=datetime.now(),
            arr_time=datetime.now(),
            price=100,
            aircraft=Aircraft.objects.first(),
        )
        Flight.objects.create(
            flight_number="UX00002",
            origin=Airport.objects.get(iata="DST"),
            destination=Airport.objects.get(iata="ORG"),
            outbound_date=datetime.strptime("2023-01-05", "%Y-%m-%d"),
            dep_time=datetime.now(),
            arr_time=datetime.now(),
            price=100,
            aircraft=Aircraft.objects.first(),
        )


    def test_passenger_details_session_data_get(self):
        """
        Simulates a GET request handled by passenger_details view.
        Tests that session data is as expected; HTTP response is 200,
        and correct template used.
        """
        data = {
            'outbound_flight':'UX00001',
            'outbound_fare':'Plus',
            'return_flight':'UX00002',
            'return_fare':'Plus',
            }
        response = self.client.get('/passenger_details/', data)
        self.assertDictEqual(dict(self.client.session), {
            'num_passengers':2,
            'next_url':'outbound_flight=UX00001&outbound_fare=Plus&return_flight=UX00002&return_fare=Plus',
            'outbound_flight':'UX00001',
            'outbound_fare':'Plus',
            'return_flight':'UX00002',
            'return_fare':'Plus',
            })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('core/passenger-details.html')



    def test_passenger_details_session_data_post(self):
        """
        Simulates a POST request handled by passenger_details view.
        Tests that session data is as expected and HTTP response is 302.
        """
        data = {
            'number-of-passengers':2,
            'passenger-1-first':'Test',
            'passenger-1-last':'McTesterson',
            'passenger-2-first':'Tester',
            'passenger-2-last':'McTesting',
            'trip-email':'test@testing.com',
            }
        response = self.client.post('/passenger_details/', data)
        self.assertDictEqual(dict(self.client.session), {
            'num_passengers':'2',
            'passengers':{
                'passenger-1':{'first':'Test', 'last':'McTesterson'},
                'passenger-2':{'first':'Tester', 'last':'McTesting'},
            },
            'trip_email':'test@testing.com',
            })
        self.assertEqual(response.status_code, 302)


