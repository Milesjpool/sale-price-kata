from mapi.SortedData import SortedData


class QueryParser(object):

    def __init__(self, data_set):
        self.__data_set = data_set

    def getDataset(self, query):
        data_set = self.__data_set
        sort_by = query.get("sort-by")
        if sort_by is not None:
            data_set = SortedData(data_set, sort_by)
        return data_set
