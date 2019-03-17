import unittest

from mock import MagicMock

from mapi.DataFile import NullDataFile, DataFile
from mapi.FileReader import FileReader


class TestDataFile(unittest.TestCase):

    def test_date_file_returns_file_data(self):
        filename = "testfile"
        expectedData = "testdata"

        file_reader = FileReader()
        file_reader.open = MagicMock(return_value=file_reader)
        file_reader.readline = MagicMock(return_value=expectedData)

        unit = DataFile(filename, file_reader)

        actualData = unit.readNext()
        file_reader.open.assert_called_with(filename)
        self.assertEqual(expectedData, actualData)

    def test_date_file_returns_file_data_without_newline(self):
        filename = "testfile"
        expectedData = "testdata"

        file_reader = FileReader()
        file_reader.open = MagicMock(return_value=file_reader)
        file_reader.readline = MagicMock(return_value=expectedData+"\n")

        unit = DataFile(filename, file_reader)

        actualData = unit.readNext()
        self.assertEqual(expectedData, actualData)

    def test_date_file_returns_None_for_empty_data(self):
        filename = "testfile"

        file_reader = FileReader()
        file_reader.open = MagicMock(return_value=file_reader)
        file_reader.readline = MagicMock(return_value="")

        unit = DataFile(filename, file_reader)

        actualData = unit.readNext()
        expectedData = None
        self.assertEqual(expectedData, actualData)

    def test_null_file_returns_null_data(self):
        unit = NullDataFile()

        expectedData = None
        actualData = unit.readNext()
        self.assertEqual(expectedData, actualData)


if __name__ == '__main__':
    unittest.main()
