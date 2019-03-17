class SortedData(object):

    def __init__(self, dataset, sort_by):
        sort = sort_by.split('-')
        raw_data = dataset.asDictionary()
        sort_key = sort[0]
        direction = sort[1] if len(sort) > 1 else "asc"

        self.__sorted_data = sorted(raw_data, key=lambda d: d[sort_key], reverse=(direction == "desc"))

    def asDictionary(self):
        return self.__sorted_data
