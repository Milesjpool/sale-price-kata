from mapi.FileReader import NullFileReader


class DataFile(object):
    def __init__(self, filepath="", filereader=NullFileReader()):
        self.__filereader = filereader.open(filepath)

    def readNext(self):
        fulline = self.__filereader.readline()
        line = fulline.rstrip()
        return line if len(line) > 0 else None


class NullDataFile(object):
    def readNext(self):
        return None
