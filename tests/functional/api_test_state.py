import docker
import requests
import time
from dotenv import load_dotenv
import os


class ApiTestState(object):
    instance_count = 0
    __host = "localhost"
    __docker_client = docker.from_env(version='auto')
    __running_container = None
    __response = None
    __error = None

    def __init__(self, test_case):
        ApiTestState.instance_count += 1
        self.__test_case = test_case

        load_dotenv(dotenv_path="config.env", verbose=True)
        self.__api_container_tag = os.getenv("TEST_BUILD")
        self.__container_port = int(os.getenv("PORT"))
        self.__cmd = os.getenv("START_COMMAND")

        self.__local_port = self.__container_port + ApiTestState.instance_count  # avoids port conflicts

    def given_the_application_is_not_running(self):
        pass

    def given_the_application_is_running(self):
        self.__start_application(self.__cmd)

    def given_the_application_is_started_with(self, args):
        self.__start_application(self.__cmd + " " + args)

    def when_I_query(self, path):
        url = 'http://{host}:{port}{path}'.format(host=self.__host, port=self.__local_port, path=path)
        print url
        try:
            self.__response = requests.get(url)
            self.__error = None
        except requests.exceptions.RequestException as e:
            self.__response = None
            self.__error = e

    def then_the_response_is_not_okay(self):
        self.__test_case.assertIsNone(self.__response, "Expected no response")
        self.__test_case.assertIsNotNone(self.__error, "Expected an error")

    def then_the_response_is_okay(self):
        self.__test_case.assertIsNotNone(self.__response, "Expected a response")
        self.__test_case.assertIsNone(self.__error, "Expected no error")
        self.__test_case.assertEqual(self.__response.status_code, 200, "Expected 200 response status.")

    def then_the_response_payload_is(self, expected_payload):
        self.__test_case.assertIsNotNone(self.__response, "Expected a response")
        self.__test_case.assertEqual(self.__response.json(), expected_payload, "Unexpected response body.")

    def tearDown(self):
        if self.__running_container is not None:
            self.__running_container.remove(force=True)
            self.__running_container = None

    def __start_application(self, start_cmd):
        port_mapping = {'{port}/tcp'.format(port=self.__container_port): self.__local_port}
        self.__running_container = self.__docker_client.containers.run(self.__api_container_tag, start_cmd,
                                                                       detach=True,
                                                                       ports=port_mapping,
                                                                       remove=True)
        time.sleep(2)
