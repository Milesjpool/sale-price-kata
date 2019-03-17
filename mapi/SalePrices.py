from mapi.DataFile import NullDataFile


class SalePrices(object):

    def __init__(self, data_file=NullDataFile()):
        self.__data = []
        self.__index = 0
        data_point = data_file.readNext()
        while data_point is not None:
            fields = data_point.split()
            fields = map(lambda x: int(x), fields)

            self.__index += 1

            self.__data.append({'id': self.__index, 'long': fields[0], 'lat': fields[1], 'price': fields[2]})
            data_point = data_file.readNext()

    def asDictionary(self):
        return self.__data
