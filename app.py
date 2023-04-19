from flask import Flask, request, jsonify
from submit_feedback import submit_feedback
from get_feedback import get_feedback
from update_feedback import update_feedback
from create_DB import create_DB
import logging

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/<userid>', methods=['POST', 'GET', 'PUT'])
def feedback(userid):
    if request.method == 'POST':
        create_DB()
        data = request.get_json()
        logging.info("POST request received!", data)
        print(data)
        resp = submit_feedback(userid, data['sessionid'], data['feedback'])
        resp = jsonify(resp)
        resp.status_code = 201
        return resp

    elif request.method == 'GET':
        create_DB()
        logging.info("GET request received!")
        resp = get_feedback(userid)
        resp = jsonify(resp)
        resp.status_code = 200
        return resp

    elif request.method == 'PUT':
        create_DB()
        data = request.get_json()
        logging.info("PUT request received!", data)
        resp = update_feedback(userid, data['feedback'])
        resp = jsonify(resp)
        resp.status_code = 200
        return resp


if __name__ == '__main__':
    app.run(debug=True)
