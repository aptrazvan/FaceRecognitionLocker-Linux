import requests
from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/test')

def get_data():
    a = requests.get('http://192.168.1.110:3000/test')
    b = a.content
    print(a)
    print(b)
    return b

@app.route('/send_image')

def send_image():
    return send_file("Untrust.jpg")

app.run(host='192.168.1.110', port=3001)
