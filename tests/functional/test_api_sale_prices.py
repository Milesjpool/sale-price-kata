import unittest
from tests.functional.api_test_state import ApiTestState


class TestApiSalePrices(unittest.TestCase):
    __data_endpoint = "/sale-prices"
    __single_data_point = [{'id': 1, 'long': 1, 'lat': 2, 'price': 3}]
    __three_data_points = [{'id': 1, 'long': 60, 'lat': 23, 'price': 3653379},
                           {'id': 2, 'long': 58, 'lat': 66, 'price': 1422640},
                           {'id': 3, 'long': 61, 'lat': 62, 'price': 5045331}]


    def setUp(self):
        self.__state = ApiTestState(self)

    def test_retrieval_of_single_raw_sale_price(self):
        self.__state.given_the_application_is_started_with("/test-data/single-data-point.txt")
        self.__state.when_I_query(self.__data_endpoint)
        self.__state.then_the_response_is_okay()
        self.__state.then_the_response_payload_is(self.__single_data_point)

    def test_retrieval_of_multiple_raw_sale_prices(self):
        self.__state.given_the_application_is_started_with("/test-data/three-data-points.txt")
        self.__state.when_I_query(self.__data_endpoint)
        self.__state.then_the_response_is_okay()
        self.__state.then_the_response_payload_is(self.__three_data_points)

    def tearDown(self):
        self.__state.tearDown()


if __name__ == '__main__':
    unittest.main()
