from flask import Flask, render_template, jsonify
import datetime

def get_sensor_data():
    temperature = 25
    humidity = 45
    pm25 = 40
    return temperature, humidity, pm25
    
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('2.html')

@app.route('/get_data')
def get_data():
    """Flask API: 아두이노 센서 데이터 제공"""
    temperature, humidity, pm25 = get_sensor_data()

    # 현재 시간 가져오기 (strftime 사용)
    now = datetime.datetime.now()
    ampm = now.strftime('%p')
    hour = now.strftime('%I').lstrip('0')
    minute = now.strftime('%M')
    second = now.strftime('%S').zfill(2)

    # JSON 응답 생성
    data = {
        "temperature": temperature,
        "humidity": humidity,
        "pm25": pm25,
        "ampm": ampm,  # 오전 또는 오후
        "hour": hour,  # 시 (01~12)
        "minute": minute,  # 분 (00~59)
        "second": second  # 초 (00~59)
    }

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
