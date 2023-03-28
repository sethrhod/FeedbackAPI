from flask import Flask, request, jsonify
from submit_feedback import submit_feedback
from get_feedback import get_feedback
from update_feedback import update_feedback

app = Flask(__name__)

@app.route('/feedback/<uuid>', methods=['POST, GET, PUT'])
def feedback():
    if request.method == 'POST':
        submit_feedback(uuid, request.form['sessionid'], request.form['feedback'])

    elif request.method == 'GET':
        resp = jsonify(get_feedback(uuid))
        resp.status_code = 200
        return resp

    elif request.method == 'PUT':
        update_feedback(uuid, request.form['feedback'])

if __name__ == '__main__':
  app.run(debug=True)
