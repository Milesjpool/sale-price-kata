import unittest

from mock import MagicMock
from mapi.SalePrices import SalePrices
from mapi.SortedData import SortedData


class TestSortedData(unittest.TestCase):

    def test_price_sort_for_single_datum(self):
        sales_prices = SalePrices()
        sales_prices.asDictionary = MagicMock(return_value=[{'id': 1, 'lat': 2, 'long': 1, 'price': 3}])
        unit = SortedData(sales_prices, "price-asc")

        expectedData = [{'id': 1, 'lat': 2, 'long': 1, 'price': 3}]
        actualData = unit.asDictionary()
        self.assertEqual(expectedData, actualData)


    def test_price_sort_ascending_for_multiple_data(self):
        sales_prices = SalePrices()
        sales_prices.asDictionary = MagicMock(return_value=[{'id': 1, 'lat': 2, 'long': 3, 'price': 6},
                                                            {'id': 2, 'lat': 1, 'long': 2, 'price': 3},
                                                            {'id': 3, 'lat': 3, 'long': 1, 'price': 9}])
        unit = SortedData(sales_prices, "price-asc")

        expectedData = [{'id': 2, 'lat': 1, 'long': 2, 'price': 3},
                        {'id': 1, 'lat': 2, 'long': 3, 'price': 6},
                        {'id': 3, 'lat': 3, 'long': 1, 'price': 9}]
        actualData = unit.asDictionary()
        self.assertEqual(expectedData, actualData)


    def test_long_sort_ascending_when_direction_is_not_defined(self):
        sales_prices = SalePrices()
        sales_prices.asDictionary = MagicMock(return_value=[{'id': 1, 'lat': 2, 'long': 3, 'price': 6},
                                                            {'id': 2, 'lat': 1, 'long': 2, 'price': 3},
                                                            {'id': 3, 'lat': 3, 'long': 1, 'price': 9}])
        unit = SortedData(sales_prices, "long")

        expectedData = [{'id': 3, 'lat': 3, 'long': 1, 'price': 9},
                        {'id': 2, 'lat': 1, 'long': 2, 'price': 3},
                        {'id': 1, 'lat': 2, 'long': 3, 'price': 6}]
        actualData = unit.asDictionary()
        self.assertEqual(expectedData, actualData)


    def test_lat_sort_descending_for_multiple_data(self):
        sales_prices = SalePrices()
        sales_prices.asDictionary = MagicMock(return_value=[{'id': 1, 'lat': 2, 'long': 3, 'price': 6},
                                                            {'id': 2, 'lat': 1, 'long': 2, 'price': 3},
                                                            {'id': 3, 'lat': 3, 'long': 1, 'price': 9}])
        unit = SortedData(sales_prices, "lat-desc")

        expectedData = [{'id': 3, 'lat': 3, 'long': 1, 'price': 9},
                        {'id': 1, 'lat': 2, 'long': 3, 'price': 6},
                        {'id': 2, 'lat': 1, 'long': 2, 'price': 3}]
        actualData = unit.asDictionary()
        self.assertEqual(expectedData, actualData)



if __name__ == '__main__':
    unittest.main()
