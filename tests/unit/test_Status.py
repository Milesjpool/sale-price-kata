import unittest
from mapi import Status


class TestStatus(unittest.TestCase):

    def setUp(self):
        self.__unit = Status.Status()

    def test_status_returns_ok(self):
        expectedStatus = {'status': 'ok'}
        actualStatus = self.__unit.asDictionary();
        self.assertEqual(expectedStatus, actualStatus)


if __name__ == '__main__':
    unittest.main()
