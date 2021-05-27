from flask import Flask, request, send_file, jsonify, Response
from check_identity import check_photo_identity
import base64

from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/test', methods=['GET', 'POST'])

def test():
    resp = Response("Success")
    resp.headers['Access-Control-Allow-Origin'] = '*'

    return resp

@app.route('/get_image', methods=['GET', 'POST'])

def get_image():
    file = request.files['image']
    file.save('Trust.jpg')

    resp = Response("Success")
    resp.headers['Access-Control-Allow-Origin'] = '*'

    return resp

@app.route('/check_identity', methods=['GET', 'POST'])

def process_request():
    file = request.files['image']
    file.save('Test.jpg')

    result = check_photo_identity('Trust.jpg', 'Test.jpg')

    if result:
        resp = Response("Success")
        resp.headers['Access-Control-Allow-Origin'] = '*'
    else:
        resp = Response("Failure")
        resp.headers['Access-Control-Allow-Origin'] = '*'


    return resp

app.run(host='192.168.1.104', port=3000)
