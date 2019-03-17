import unittest
from tests.functional.api_test_state import ApiTestState


class TestApiPriceBreakdown(unittest.TestCase):
    __data_endpoint_price_asc = "/sale-prices?sort-by=price-asc"
    __three_data_points_price_asc = [{'id': 2, 'long': 58, 'lat': 66, 'price': 1422640},
                                     {'id': 1, 'long': 60, 'lat': 23, 'price': 3653379},
                                     {'id': 3, 'long': 61, 'lat': 62, 'price': 5045331}]

    __data_endpoint_price_desc = "/sale-prices?sort-by=price-desc"
    __three_data_points_price_desc = [{'id': 3, 'long': 61, 'lat': 62, 'price': 5045331},
                                      {'id': 1, 'long': 60, 'lat': 23, 'price': 3653379},
                                      {'id': 2, 'long': 58, 'lat': 66, 'price': 1422640}]

    def setUp(self):
        self.__state = ApiTestState(self)

    def test_sort_by_price_ascending(self):
        self.__state.given_the_application_is_started_with("/test-data/three-data-points.txt")
        self.__state.when_I_query(self.__data_endpoint_price_asc)
        self.__state.then_the_response_is_okay()
        self.__state.then_the_response_payload_is(self.__three_data_points_price_asc)

    def test_sort_by_price_descending(self):
        self.__state.given_the_application_is_started_with("/test-data/three-data-points.txt")
        self.__state.when_I_query(self.__data_endpoint_price_desc)
        self.__state.then_the_response_is_okay()
        self.__state.then_the_response_payload_is(self.__three_data_points_price_desc)

    def tearDown(self):
        self.__state.tearDown()


if __name__ == '__main__':
    unittest.main()
