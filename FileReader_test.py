import unittest
from FileReader import FileReader


class TestFileReader(unittest.TestCase):
    def test_reader(self):
        fileReader = FileReader()
        fileName = "demofile.txt"
        data = []
        data.append("hello")
        data.append("w")
        fileReader.getFileContent(fileName)
        self.assertEqual(fileReader.getData(), data)
