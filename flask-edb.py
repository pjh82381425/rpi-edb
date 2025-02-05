from lib import get_temperature, get_humidity, get_pm25
from flask import Flask, render_template, jsonify
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    temperature = get_temperature()
    humidity = get_humidity()
    pm25 = get_pm25()
    
    # 현재 시간 가져오기
    current_time = datetime.datetime.now().strftime('%H:%M:%S')

    # 반환할 데이터
    data = {
        "temperature": temperature,
        "humidity": humidity,
        "pm25": pm25,
        "current_time": current_time
    }
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
