# 
from lib import read
from flask import Flask, render_template, jsonify
import datetime
import logging
import traceback

logging.basicConfig(filename='./Error.log', level=logging.ERROR)

app = Flask(__name__)

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except:
        logging.error(traceback.format_exc())
        return "Loading Error : index.html"

@app.route('/get_time')
def get_time():
    try:
        # 현재 시간 가져오기
        now = datetime.datetime.now()
        ampm = now.strftime('%p')
        hour = now.strftime('%I').lstrip('0')
        minute = now.strftime('%M')
        second = now.strftime('%S').zfill(2)
    
        # JSON 응답 생성
        data = {
            "ampm": ampm,  # 오전 또는 오후
            "hour": hour,  # 시 (01~12)
            "minute": minute,  # 분 (00~59)
            "second": second  # 초 (00~59)
        }

        return jsonify(data)
    except:
            logging.error(traceback.format_exc())
            return None

@app.route('/get_hour_24')
def get_hour_24():
    try:
        now = datetime.datetime.now()
        hour_24 = now.strftime('%H')
    
        # JSON 응답 생성
        data = {
            "hour_24" : hour_24
        }

        return jsonify(data)
    except:
        logging.error(traceback.format_exc())
        return None

@app.route('/get_data')
def get_data():
    try:
        """Flask API: 아두이노 센서 데이터 제공"""
        temperature, humidity, pm25 = read()

        # JSON 응답 생성
        data = {
            "temperature": temperature,
            "humidity": humidity,
            "pm25": pm25
        }

        return jsonify(data)
    except:
        logging.error(traceback.format_exc())
        return None

@app.route('/get_ver')
def get_ver():
    # JSON 응답 생성
    data = {
        "ver": "ver = 0.2.2"
    }

    return jsonify(data)

if __name__ == '__main__':
    try:
        # app.run(host='0.0.0.0', port=5001, debug=True)
        app.run(host='0.0.0.0', port=5001, threaded=True) # 성능 최적화
    except:
        logging.error(traceback.format_exc())
        print("Flask Server Error")