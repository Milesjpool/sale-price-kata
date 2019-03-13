import unittest
from tests.functional.api_test_state import ApiTestState


class TestApiStatus(unittest.TestCase):
    __status_endpoint = "/status"
    __expected_body = {u'status': u"ok"}

    def setUp(self):
        self.__state = ApiTestState(self)

    def test_status_gives_no_response_when_not_running(self):
        self.__state.given_the_application_is_not_running()
        self.__state.when_I_query(self.__status_endpoint)
        self.__state.then_the_response_is_not_okay()

    def test_status_gives_okay_response_when_running(self):
        self.__state.given_the_application_is_running()
        self.__state.when_I_query(self.__status_endpoint)
        self.__state.then_the_response_is_okay()
        self.__state.then_the_response_payload_is(self.__expected_body)

    def tearDown(self):
        self.__state.tearDown()


if __name__ == '__main__':
    unittest.main()
