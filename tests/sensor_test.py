import unittest
from pandas import DataFrame
from datetime import datetime
from src.sensor import Visitors

class TestVisitSensor(unittest.TestCase):

    def test_generate_data_as_df(self):
        visitors = Visitors()
        self.assertEqual(type(visitors.generate_data("df")), DataFrame)

    def test_generate_data_as_dict(self):
        visitors = Visitors()
        self.assertEqual(type(visitors.generate_data("dict")), dict)

    def test_number_of_day(self):
        visitors = Visitors()
        nb_day = (datetime.now() - datetime(2020, 1, 1)).days
        df = visitors.generate_data("df")
        nb_day_dataframe = df.groupby("day").count().shape[0]

        self.assertEqual(nb_day, nb_day_dataframe)

    def test_sunday_closed(self):
        visitors = Visitors()
        visit_count = visitors.get_number_visitors("2025-06-15", 10, "Paris")
        self.assertFalse(visit_count)

    def test_day_open(self):
        visitors = Visitors()
        visit_count = visitors.get_number_visitors("2025-06-07", 10, "Paris")
        self.assertEqual(visit_count, 81)

    def test_breakdown(self):
        visitors = Visitors()
        visit_count = visitors.get_number_visitors("2020-01-13", 12, "Paris")
        self.assertTrue(visit_count)
