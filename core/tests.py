from django.test import TestCase, Client
from .models import *
from datetime import datetime
from .views import *
from users.models import *


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
        response = self.client.get(
            "/search_results/",
            {
                "passengers": "5",
                "trip_type": "return",
                "origin": "(ORG)",
                "destination": "(DST)",
                "outbound_date": "2023-01-10",
                "return_date": "2023-02-10",
            },
        )
        self.assertDictEqual(
            dict(self.client.session),
            {
                "num_passengers": 5,
                "trip_type": "return",
                "outbound_date": "2023-01-10",
                "outbound_previous_date": "2023-01-10",
                "return_date": "2023-02-10",
                "return_previous_date": "2023-02-10",
            },
        )

    def test_oneway_trip(self):
        """
        Tests context for one-way trip option.
        """
        response = self.client.get(
            "/search_results/",
            {
                "passengers": "5",
                "trip_type": "oneway",
                "origin": "(ORG)",
                "destination": "(DST)",
                "outbound_date": "2023-01-10",
            },
        )
        self.assertDictEqual(
            dict(self.client.session),
            {
                "num_passengers": 5,
                "trip_type": "oneway",
                "outbound_date": "2023-01-10",
                "outbound_previous_date": "2023-01-10",
            },
        )


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
        session["num_passengers"] = 2
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
            "outbound_flight": "UX00001",
            "outbound_fare": "Plus",
            "return_flight": "UX00002",
            "return_fare": "Plus",
        }
        response = self.client.get("/passenger_details/", data)
        self.assertDictEqual(
            dict(self.client.session),
            {
                "num_passengers": 2,
                "next_url": "outbound_flight=UX00001&outbound_fare=Plus&return_flight=UX00002&return_fare=Plus",
                "outbound_flight": "UX00001",
                "outbound_fare": "Plus",
                "return_flight": "UX00002",
                "return_fare": "Plus",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("core/passenger-details.html")

    def test_passenger_details_session_data_post(self):
        """
        Simulates a POST request handled by passenger_details view.
        Tests that session data is as expected and HTTP response is 302.
        """
        data = {
            "number-of-passengers": 2,
            "passenger-1-first": "Test",
            "passenger-1-last": "McTesterson",
            "passenger-2-first": "Tester",
            "passenger-2-last": "McTesting",
            "trip-email": "test@testing.com",
        }
        response = self.client.post("/passenger_details/", data)
        self.assertDictEqual(
            dict(self.client.session),
            {
                "num_passengers": "2",
                "passengers": {
                    "passenger-1": {"first": "Test", "last": "McTesterson"},
                    "passenger-2": {"first": "Tester", "last": "McTesting"},
                },
                "trip_email": "test@testing.com",
            },
        )
        self.assertEqual(response.status_code, 302)

    def test_valid_num_passengers(self):
        """
        Tests that passenger_details view returns 200 for valid num_passengers.
        Tests range of 0-10 and appends result to check_list.
        Tests that check_list is as expected.
        """
        data = {
            "outbound_flight": "UX00001",
            "outbound_fare": "Plus",
            "return_flight": "UX00002",
            "return_fare": "Plus",
        }
        session = self.client.session
        check_list = []
        for n in range(0, 10):
            session["num_passengers"] = n
            session.save()
            response = self.client.get("/passenger_details/", data)
            if response.status_code == 200:
                check_list.append(True)
            else:
                check_list.append(False)
        self.assertListEqual(
            check_list, [False, True, True, True, True, True, True, True, True, False]
        )


class AltDatesViewTestCase(TestCase):
    """
    Test case for alt_dates view. Tests htmx requests on search results page.
    """

    def setUp(self):
        """
        Initiates Client and test data.
        """
        self.client = Client()
        session = self.client.session
        session["trip_type"] = "oneway"
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
            outbound_date=datetime.strptime("2023-01-10", "%Y-%m-%d"),
            dep_time=datetime.now(),
            arr_time=datetime.now(),
            price=100,
            aircraft=Aircraft.objects.first(),
        )

    def test_flight_results(self):
        """
        Tests that Flight results for the chosen alt_date are as intended.
        """
        data = {
            "leg": "outbound",
            "origin": "(ORG)",
            "destination": "(DST)",
            "date": "2023-01-05",
        }
        response = self.client.get("/search_results/alt_dates/", data)
        flight_results = response.context["flight_results"]
        self.assertQuerysetEqual(
            flight_results,
            Flight.objects.filter(flight_number="UX00001"),
            ordered=False,
        )

    def test_flight_results(self):
        """
        Tests that Flight results for the chosen alt_date are as intended.
        """
        data = {
            "leg": "outbound",
            "origin": "(ORG)",
            "destination": "(DST)",
            "date": "2023-01-05",
        }
        response = self.client.get("/search_results/alt_dates/", data)
        flight_results = response.context["flight_results"]
        self.assertQuerysetEqual(
            flight_results,
            Flight.objects.filter(flight_number="UX00001"),
            ordered=False,
        )

    def test_slider_date_list(self):
        """
        Tests that new list of dates shown in alt_date_slider on search results
        page is as intended.
        """
        data = {
            "leg": "outbound",
            "origin": "(ORG)",
            "destination": "(DST)",
            "date": "2023-01-05",
        }
        response = self.client.get("/search_results/alt_dates/", data)
        date_list = response.context["slider_date_list"]
        self.assertListEqual(
            date_list,
            [
                datetime.strptime("2023-01-03", "%Y-%m-%d"),
                datetime.strptime("2023-01-04", "%Y-%m-%d"),
                datetime.strptime("2023-01-05", "%Y-%m-%d"),
                datetime.strptime("2023-01-06", "%Y-%m-%d"),
                datetime.strptime("2023-01-07", "%Y-%m-%d"),
            ],
        )

    def test_template_and_response(self):
        """
        Tests that correct response and template used.
        """
        data = {
            "leg": "outbound",
            "origin": "(ORG)",
            "destination": "(DST)",
            "date": "2023-01-05",
        }
        response = self.client.get("/search_results/alt_dates/", data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("partials/flights.html")

    def test_invalid_date_selection(self):
        """
        Tests that same flight results as previous request are returned if invalid dates are selected.
        """
        session = self.client.session
        session["trip_type"] = "return"
        session["outbound_date"] = "2023-01-05"
        session["outbound_previous_date"] = "2023-01-05"
        session["return_date"] = "2023-01-06"
        session.save()
        data = {
            "leg": "outbound",
            "origin": "(ORG)",
            "destination": "(DST)",
            "date": "2023-01-07",
        }
        response = self.client.get("/search_results/alt_dates/", data)
        flight_results = response.context["flight_results"]
        self.assertQuerysetEqual(
            flight_results,
            Flight.objects.filter(outbound_date="2023-01-05"),
            ordered=False,
        )

    def test_invalid_date_selection_return(self):
        """
        Tests that same flight results as previous request are returned if invalid dates are selected.
        """
        session = self.client.session
        session["trip_type"] = "return"
        session["outbound_date"] = "2023-01-05"
        session["outbound_previous_date"] = "2023-01-05"
        session["return_date"] = "2023-01-06"
        session["return_previous_date"] = "2023-01-06"
        session.save()
        data = {
            "leg": "return",
            "origin": "(ORG)",
            "destination": "(DST)",
            "date": "2023-01-04",
        }
        response = self.client.get("/search_results/alt_dates/", data)
        flight_results = response.context["flight_results"]
        self.assertQuerysetEqual(
            flight_results,
            Flight.objects.filter(outbound_date="2023-01-06"),
            ordered=False,
        )


class AboutPageViewTestCase(TestCase):
    """
    Tests template and status code for about page view.
    """

    def test_about_view(self):
        self.client = Client()
        response = self.client.get("/about/")
        self.assertTemplateUsed("base/about.html")
        self.assertEqual(response.status_code, 200)


class CheckoutViewTestCase(TestCase):
    """
    Tests template and status code for checkout view.
    Tests booking creation and session data.
    """

    def setUp(self):
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
            outbound_date=datetime.strptime("2023-01-10", "%Y-%m-%d"),
            dep_time=datetime.now(),
            arr_time=datetime.now(),
            price=100,
            aircraft=Aircraft.objects.first(),
        )

        self.client = Client()
        self.client.force_login(
            user=User.objects.create_user(
                email="testuser@test.com",
                first_name="test",
                last_name="test",
                password="12345",
            )
        )
        session = self.client.session
        session["passengers"] = {
            "passenger-1": {"first": "Test", "last": "McTesterson"},
            "passenger-2": {"first": "Tester", "last": "McTesting"},
        }
        session["outbound_flight"] = "UX00001"
        session["outbound_fare"] = "Plus"
        session["num_passengers"] = 2
        session["trip_type"] = "return"
        session["return_flight"] = "UX00002"
        session["return_fare"] = "Plus"
        session["trip_email"] = "testuser@test.com"
        session.save()

    def test_booking_created_return(self):
        """
        Tests that booking is created with correct trip type (one-way).
        """
        self.assertEqual(Booking.objects.count(), 0)
        request = self.client.post("/checkout/")
        self.assertEqual(Booking.objects.count(), 1)
        self.assertEqual(
            Booking.objects.first().return_flight,
            Flight.objects.get(flight_number="UX00002"),
        )

    def test_booking_created_oneway(self):
        """
        Tests that booking is created with correct trip type (one-way).
        """
        session = self.client.session
        session["trip_type"] = "oneway"
        session.save()

        self.assertEqual(Booking.objects.count(), 0)
        request = self.client.post("/checkout/")
        self.assertEqual(Booking.objects.count(), 1)
        self.assertEqual(Booking.objects.first().return_flight, None)

    def test_template_and_response(self):
        """
        Tests that correct response and template used.
        """
        response = self.client.get("/checkout/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("checkout/checkout.html")


class OrderConfirmationViewTestCase(TestCase):
    """
    Tests order confirmation view.
    Tests that error is raised if user unauthorised.
    """

    def setUp(self):
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
            outbound_date=datetime.strptime("2023-01-10", "%Y-%m-%d"),
            dep_time=datetime.now(),
            arr_time=datetime.now(),
            price=100,
            aircraft=Aircraft.objects.first(),
        )
        User.objects.create_user(
            email="testuser@test.com",
            first_name="test",
            last_name="test",
            password="12345",
        )
        self.client = Client()

        Booking.objects.create(
            outbound_flight=Flight.objects.get(flight_number="UX00001"),
            return_flight=Flight.objects.get(flight_number="UX00002"),
            customer=User.objects.get(first_name="test"),
        )

    def test_order_confirmation_view_context(self):
        """
        Tests that order confirmation view context contains correct booking.
        """
        self.client.force_login(user=User.objects.get(first_name="test"))
        booking = Booking.objects.get(
            outbound_flight=Flight.objects.get(flight_number="UX00001")
        )
        response = self.client.get(f"/order_confirmation/{booking.id}")
        self.assertEqual(response.context["booking"], booking)

    def test_unauthorised_user(self):
        """
        Tests that unauthorised user cannot access order confirmation page.
        """
        User.objects.create_user(
            email="unauth@test.com",
            first_name="unauth",
            last_name="test",
            password="12345",
        )
        booking = Booking.objects.get(
            outbound_flight=Flight.objects.get(flight_number="UX00001")
        )
        self.client.force_login(user=User.objects.get(first_name="unauth"))
        response = self.client.get(f"/order_confirmation/{booking.id}")
        self.assertEqual(response.status_code, 403)


class BookingsViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
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
            outbound_date=datetime.strptime("2023-01-10", "%Y-%m-%d"),
            dep_time=datetime.now(),
            arr_time=datetime.now(),
            price=100,
            aircraft=Aircraft.objects.first(),
        )
        User.objects.create_user(
            email="testuser@test.com",
            first_name="test",
            last_name="test",
            password="12345",
        )

        User.objects.create_user(
            email="testuser2@test.com",
            first_name="test2",
            last_name="test2",
            password="12345",
        )

        Booking.objects.create(
            outbound_flight=Flight.objects.get(flight_number="UX00001"),
            return_flight=Flight.objects.get(flight_number="UX00002"),
            customer=User.objects.get(first_name="test"),
        )

        Booking.objects.create(
            outbound_flight=Flight.objects.get(flight_number="UX00001"),
            return_flight=Flight.objects.get(flight_number="UX00002"),
            customer=User.objects.get(first_name="test2"),
        )

    def test_bookings_view_context(self):
        """
        Tests that only user's bookings are returned.
        """
        self.client.force_login(user=User.objects.get(first_name="test"))
        response = self.client.get("/bookings/")
        self.assertQuerysetEqual(
            response.context["bookings"],
            Booking.objects.filter(customer=response.context["user"]),
        )


class BookingsDetailViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
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
            outbound_date=datetime.strptime("2023-01-10", "%Y-%m-%d"),
            dep_time=datetime.now(),
            arr_time=datetime.now(),
            price=100,
            aircraft=Aircraft.objects.first(),
        )
        User.objects.create_user(
            email="testuser@test.com",
            first_name="test",
            last_name="test",
            password="12345",
        )

        User.objects.create_user(
            email="testuser2@test.com",
            first_name="test2",
            last_name="test2",
            password="12345",
        )

        Booking.objects.create(
            outbound_flight=Flight.objects.get(flight_number="UX00001"),
            return_flight=Flight.objects.get(flight_number="UX00002"),
            customer=User.objects.get(first_name="test"),
        )

        Booking.objects.create(
            outbound_flight=Flight.objects.get(flight_number="UX00001"),
            return_flight=Flight.objects.get(flight_number="UX00002"),
            customer=User.objects.get(first_name="test2"),
        )

    def test_unauthorised_user(self):
        """
        Tests that an unauthorised user cannot access the bookings detail page.
        """
        self.client.force_login(User.objects.get(first_name="test"))
        booking = Booking.objects.get(customer=User.objects.get(first_name="test2"))
        response = self.client.get(f"/bookings/detail/{booking.id}")
        self.assertEqual(response.status_code, 403)

    def test_cancel_booking(self):
        """
        Tests that a booking can be cancelled and deleted from database.
        """
        self.client.force_login(User.objects.get(first_name="test"))
        booking = Booking.objects.get(customer=User.objects.get(first_name="test"))
        response = self.client.delete(f"/bookings/detail/{booking.id}")
        self.assertQuerysetEqual(
            Booking.objects.filter(customer=User.objects.get(first_name="test")), []
        )
        self.assertEqual(response.status_code, 200)

    def test_authorised_user(self):
        """
        Tests that an authorised user can access the bookings detail page.
        """
        self.client.force_login(User.objects.get(first_name="test"))
        booking = Booking.objects.get(customer=User.objects.get(first_name="test"))
        response = self.client.get(f"/bookings/detail/{booking.id}")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/bookings-detail.html")
        self.assertEqual(response.context["booking"], booking)


class BookingsEditViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
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
            outbound_date=datetime.strptime("2023-01-10", "%Y-%m-%d"),
            dep_time=datetime.now(),
            arr_time=datetime.now(),
            price=100,
            aircraft=Aircraft.objects.first(),
        )
        User.objects.create_user(
            email="testuser@test.com",
            first_name="test",
            last_name="test",
            password="12345",
        )

        User.objects.create_user(
            email="testuser2@test.com",
            first_name="test2",
            last_name="test2",
            password="12345",
        )

        Booking.objects.create(
            outbound_flight=Flight.objects.get(flight_number="UX00001"),
            return_flight=Flight.objects.get(flight_number="UX00002"),
            customer=User.objects.get(first_name="test"),
        )

        Booking.objects.create(
            outbound_flight=Flight.objects.get(flight_number="UX00001"),
            return_flight=Flight.objects.get(flight_number="UX00002"),
            customer=User.objects.get(first_name="test2"),
        )

        Passenger.objects.create(
            booking=Booking.objects.get(customer=User.objects.get(first_name="test")),
            first="test_first",
            last="test_last",
        )

    def test_unauthorised_user(self):
        """
        Tests that an unauthorised user cannot access the bookings edit page.
        """
        self.client.force_login(User.objects.get(first_name="test"))
        booking = Booking.objects.get(customer=User.objects.get(first_name="test2"))
        response = self.client.get(f"/bookings/detail/{booking.id}")
        self.assertEqual(response.status_code, 403)

    def test_authorised_user(self):
        """
        Tests that an authorised user can access the bookings edit page.
        """
        self.client.force_login(User.objects.get(first_name="test"))
        booking = Booking.objects.get(customer=User.objects.get(first_name="test"))
        response = self.client.get(f"/bookings/detail/{booking.id}")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/bookings-detail.html")
        self.assertEqual(response.context["booking"], booking)

    def test_edit_booking(self):
        """
        Tests that a booking can be edited with updated passenger names.
        """
        self.client.force_login(User.objects.get(first_name="test"))
        booking = Booking.objects.get(customer=User.objects.get(first_name="test"))
        passenger = Passenger.objects.get(booking=booking)
        data = {
            f"first-{passenger.id}": "updated_first",
            f"last-{passenger.id}": "updated_last",
        }
        response = self.client.post(f"/bookings/detail/edit/{booking.id}", data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["passengers"][0].first, "updated_first")
        self.assertEqual(response.context["passengers"][0].last, "updated_last")
