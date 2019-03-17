import unittest
from mock import MagicMock
from mapi import SalePrices
from mapi.DataFile import DataFile


class TestStatus(unittest.TestCase):

    def setUp(self):
        self.__data_file = DataFile()
        self.__unit = SalePrices.SalePrices(self.__data_file)

    def test_sale_prices_returns_single_data(self):
        self.__data_file.readLine = MagicMock(return_value="1 2 3")
        expectedData = [{'id': 1, 'lat': 2, 'long': 1, 'price': 3}]
        actualData = self.__unit.asDictionary()
        self.assertEqual(expectedData, actualData)


if __name__ == '__main__':
    unittest.main()
