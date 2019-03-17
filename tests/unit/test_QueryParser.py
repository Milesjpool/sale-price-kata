import unittest

from mock import MagicMock

from mapi.SortedData import SortedData
from mapi.QueryParser import QueryParser
from mapi.SalePrices import SalePrices


class TestQueryParser(unittest.TestCase):

    def test_query_parser_returns_regular_dataset(self):
        expected_data_set = SalePrices()
        unit = QueryParser(expected_data_set)

        query = MockArgs({"unknown-arg", "value"})
        query.get = MagicMock(return_value=None)

        actual_data_set = unit.getDataset(query)
        self.assertEqual(expected_data_set, actual_data_set)

    def test_query_parser_returns_sorted_dataset(self):
        data_set = SalePrices()
        unit = QueryParser(data_set)

        query = MockArgs({'sort-by': 'value'})

        actual_data_set = unit.getDataset(query)
        self.assertIsInstance(actual_data_set, SortedData)


class MockArgs(object):
    def __init__(self, args):
        self.args = args

    def get(self, key):
        return self.args[key]


if __name__ == '__main__':
    unittest.main()
