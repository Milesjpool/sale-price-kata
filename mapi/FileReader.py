class FileReader(object):
    def __init__(self):
        self.__file = NullFileReader()

    def open(self, filepath):
        self.__file = open(filepath, 'r')
        return self

    def readline(self):
        return self.__file.readline()


class NullFileReader(object):
    def open(self, filepath):
        return self

    def readline(self):
        return None
