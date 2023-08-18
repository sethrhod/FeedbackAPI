from flask import Flask, request, jsonify, send_file, redirect
from submit_feedback import submit_feedback
from get_feedback import get_feedback
from update_feedback import update_feedback
from delete_feedback import delete_feedback
from create_DB import create_DB
import logging
import json
import os

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/<userid>', methods=['POST', 'GET', 'PUT', 'DELETE'])
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
        resp = update_feedback(
            userid, data['sessionid'], data['feedback'], data['original_feedback'])
        resp = jsonify(resp)
        resp.status_code = 200
        return resp

    elif request.method == "DELETE":
        create_DB()
        data = request.get_json()
        logging.info("DELETE request received!", data)
        resp = delete_feedback(userid, data['sessionid'], data['feedback'])
        resp = jsonify(resp)
        resp.status_code = 200
        return resp


@app.route('/events', methods=['GET'])
def events():
    if request.method == 'GET':
        with open('event_bundles/events.json') as json_file:
            events = json.load(json_file)
            resp = jsonify(events)
            resp.status_code = 200
            return resp


@app.route('/download/<path:zip>', methods=['GET'])
def download(zip):
    if os.path.isfile(zip):
        try:
            return send_file(zip, as_attachment=True)
        except Exception as e:
            print(str(e))
            resp = jsonify({"message": "Error in downloading file",
                            "status_code": 500
                            })
            return resp
    else:
        print("File not found")
        # 404 file not found
        resp = jsonify({"message": "File not found",
                        "status_code": 404
                        })
        return resp


@app.route('/qr_redirect')
def qr_redirect():
    user_agent = request.headers.get('User-Agent', '')

    if 'iPhone' in user_agent or 'iPad' in user_agent:
        # Redirect to the App Store listing for iOS
        return redirect('https://apps.apple.com/us/app/atc-conferences/id6450556298', code=302)
    elif 'Android' in user_agent:
        # Redirect to the Play Store listing for Android
        return redirect('https://play.google.com/store/apps/details?id=com.qimatatech.atcconferences&hl=en_US&gl=US', code=302)
    else:
        # If device not recognized, redirect to a generic page
        return redirect('https://www.atldevcon.com/', code=302)


if __name__ == '__main__':
    app.run(debug=True)
