import unittest
from mapi import status


class TestStatus(unittest.TestCase):

    def setUp(self):
        self.__unit = status.Status();

    def test_status_returns_ok_json(self):
        expectedStatus = {'status': 'ok'}
        actualStatus = self.__unit.asDictionary();
        self.assertEqual(expectedStatus, actualStatus)


if __name__ == '__main__':
    unittest.main()
