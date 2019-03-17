import sys
from flask import Flask
from flask import jsonify
from flask import request

from mapi.DataFile import DataFile, NullDataFile
from mapi.FileReader import FileReader
from mapi.QueryParser import QueryParser
from mapi.SalePrices import SalePrices
from mapi.Status import Status

server = Flask(__name__)

status = Status()

data_file = NullDataFile()
if len(sys.argv) > 1:
    data_file = DataFile(sys.argv[1], FileReader())

sale_prices = SalePrices(data_file)
query_parser = QueryParser(sale_prices)

@server.route("/status")
def _status():
    return jsonify(status.asDictionary())


@server.route("/sale-prices")
def _sale_prices():
    data_set = query_parser.getDataset(request.args)
    return jsonify(data_set.asDictionary())

if __name__ == "__main__":
    server.run(host='0.0.0.0')
