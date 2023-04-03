from flask import Flask, request, jsonify
from submit_feedback import submit_feedback
from get_feedback import get_feedback
from update_feedback import update_feedback
from create_DB import create_DB
import ssl

priv_key = '/home/seth/certs/myCA.key'
cert = '/home/seth/certs/myCA.pem'
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain(cert, priv_key)

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/<userid>')
def feedback():
    if request.method == 'POST':
        resp = jsonify(submit_feedback(userid, request.form['sessionid'], request.form['feedback']))
        resp.status_code = 201
        return resp

    elif request.method == 'GET':
        resp = jsonify(get_feedback(userid))
        resp.status_code = 200
        return resp

    elif request.method == 'PUT':
        resp = jsonify(update_feedback(userid, request.form['feedback']))
        resp.status_code = 200
        return resp

if __name__ == '__main__':
    create_DB()
    app.run(debug=True, ssl_context=context)