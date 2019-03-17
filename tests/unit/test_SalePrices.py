import unittest
from mock import MagicMock
from mapi import SalePrices
from mapi.DataFile import DataFile


class TestSalePrices(unittest.TestCase):

    def test_sale_prices_returns_single_datum(self):
        data_file = DataFile()
        data_file.readNext = MagicMock(side_effect=["1 2 3", None])
        unit = SalePrices.SalePrices(data_file)

        expectedData = [{'id': 1, 'lat': 2, 'long': 1, 'price': 3}]
        actualData = unit.asDictionary()
        self.assertEqual(expectedData, actualData)

    def test_sale_prices_returns_multiple_data(self):
        data_file = DataFile()
        data_file.readNext = MagicMock(side_effect=["1 2 3", "4 5 6", "7 8 9", None])
        unit = SalePrices.SalePrices(data_file)

        expectedData = [{'id': 1, 'lat': 2, 'long': 1, 'price': 3},
                        {'id': 2, 'lat': 5, 'long': 4, 'price': 6},
                        {'id': 3, 'lat': 8, 'long': 7, 'price': 9}]
        actualData = unit.asDictionary()
        self.assertEqual(expectedData, actualData)



if __name__ == '__main__':
    unittest.main()
