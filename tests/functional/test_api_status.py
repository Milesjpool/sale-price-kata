import unittest
import requests


class TestApiStatus(unittest.TestCase):
    __status_endpoint = "/status"

    def test_status_gives_no_response_when_not_running(self):
        self.__given_the_application_is_not_running()
        self.__when_I_query(self.__status_endpoint)
        self.__then_the_response_is_not_okay()

    __host = "localhost"
    __port = "8080"

    def __given_the_application_is_not_running(self):
        pass

    def __when_I_query(self, path):
        url = 'http://{host}:{port}{path}'.format(host=self.__host, port=self.__port, path=path)
        try:
            self.response = requests.get(url)
            self.error = None
        except requests.exceptions.RequestException as e:
            self.response = None
            self.error = e

    def __then_the_response_is_not_okay(self):
        self.assertIsNone(self.response, "Expected no response")
        self.assertIsNotNone(self.error, "Expected an error")


if __name__ == '__main__':
    unittest.main()
