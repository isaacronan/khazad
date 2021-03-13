from flask import Flask, jsonify, request
from utils import fromjson

application = Flask(__name__)

@application.route('/config', methods=['POST'])
def getdata():
    body = request.get_json()
    data = fromjson(body).resolve()
    return jsonify(data)

@application.errorhandler(500)
def handleservererror(error):
    return error, 500

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8011)