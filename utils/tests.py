from django.test import TestCase
from altdates import create_alt_date_range
from datetime import datetime


class AltDatesTestCase(TestCase):

    def test_slider_dates_list_length(self):
        list = create_alt_date_range('2023-10-10')
        self.assertTrue(len(list), 5)

    def test_dates_range(self):
        list = create_alt_date_range('2023-10-10')
        str_list = []
        for date in list:
            str_list.append(datetime.strftime(date, '%Y-%m-%d'))
        self.assertListEqual(str_list, ['2023-10-08','2023-10-09','2023-10-10','2023-10-11','2023-10-12'])
