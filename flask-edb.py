
# 아침 점심 저녁 아이콘, read 완성해야 함

# from lib import read
from flask import Flask, render_template, jsonify
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    """Flask API: 아두이노 센서 데이터 제공"""
    pm25 = 10

    # 현재 시간 가져오기 (strftime 사용)
    now = datetime.datetime.now()
    ampm = now.strftime('%p')
    hour_24 = now.strftime('%H')
    hour = now.strftime('%I').lstrip('0')
    minute = now.strftime('%M')
    second = now.strftime('%S').zfill(2)
    
    # environment_data = read()
    # temperature, humidity = map(int, environment_data.split(','))
    environment_data = 32, 10
    temperature, humidity = environment_data
    
    # JSON 응답 생성
    data = {
        "temperature": temperature,
        "humidity": humidity,
        "pm25": pm25,
        "ampm": ampm,  # 오전 또는 오후
        "hour_24" : hour_24,
        "hour": hour,  # 시 (01~12)
        "minute": minute,  # 분 (00~59)
        "second": second  # 초 (00~59)
    }

    return jsonify(data)

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000, debug=True)
    app.run(host='0.0.0.0', port=5000, threaded=True) # 성능 최적화  

