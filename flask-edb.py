from lib import read
from flask import Flask, render_template, jsonify
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_time')
def get_time():
    now = datetime.datetime.now()
    ampm = now.strftime('%p')
    hour = now.strftime('%I').lstrip('0')
    minute = now.strftime('%M')
    second = now.strftime('%S').zfill(2)
    
    data = {
        "ampm": ampm,
        "hour": hour,
        "minute": minute,
        "second": second
    }

    return jsonify(data)

@app.route('/get_hour_24')
def get_hour_24():
    now = datetime.datetime.now()
    hour_24 = now.strftime('%H')
    
    data = {
        "hour_24": hour_24
    }

    return jsonify(data)

@app.route('/get_data')
def get_data():
    temperature, humidity, pm25 = read()
    
    data = {
        "temperature": temperature,
        "humidity": humidity,
        "pm25": pm25
    }

    return jsonify(data)

@app.route('/get_ver')
def get_ver():
    data = {
        "ver": "ver = 0.2.2"
    }

    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, threaded=True)
