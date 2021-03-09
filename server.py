from flask import Flask, jsonify, request
from creator import create

application = Flask(__name__)

@application.route('/data', methods=['POST'])
def getsubscription():
    body = request.get_json()
    data = create(body).resolve()
    return jsonify(data)

@application.errorhandler(404)
def handlenotfound(error):
    return jsonify({ 'error': 'Route not found.' }), 404

@application.errorhandler(500)
def handleservererror(error):
    return jsonify({ 'error': 'Server error encountered.' }), 500

if __name__ == '__main__':
    application.run(host='0.0.0.0')