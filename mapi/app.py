from flask import Flask
from flask import jsonify
from mapi.status import Status

server = Flask(__name__)
serverStatus = Status()

@server.route("/status")
def status():
    return jsonify(serverStatus.asDictionary())


if __name__ == "__main__":
    server.run(host='0.0.0.0')
