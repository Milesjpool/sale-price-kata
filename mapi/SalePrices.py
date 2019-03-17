class SalePrices(object):

    def __init__(self, data_reader):
        self.__data = []
        self.__data.append({'id': 1, 'long': 1, 'lat': 2, 'price': 3})

    def asDictionary(self):
        return self.__data
