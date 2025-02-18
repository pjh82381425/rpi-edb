# http://10.103.77.127:5000
from lib import read
from flask import Flask, render_template, jsonify
import datetime
import logging

logging.basicConfig(filename='error.log', level=logging.ERROR, 
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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
    except Exception as e:
        logger.error("Error in /get_time: %s", e)
        return jsonify({"error": "An error occurred"}), 500

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
    except Exception as e:
        logger.error("Error in /get_hour_24: %s", e)
        return jsonify({"error": "An error occurred"}), 500

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
    except Exception as e:
        logger.error("Error in /get_data: %s", e)
        return jsonify({"error": "An error occurred"}), 500

@app.route('/get_ver')
def get_ver():
    try:
        # JSON 응답 생성
        data = {
            "ver": "ver = 0.2.3"
        }

        return jsonify(data)
    except Exception as e:
        logger.error("Error in /get_ver: %s", e)
        return jsonify({"error": "An error occurred"}), 500

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5001, debug=True)
    app.run(host='0.0.0.0', port=5001, threaded=True) # 성능 최적화
