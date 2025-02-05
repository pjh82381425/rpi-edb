from flask import Flask, render_template, jsonify
import serial
import time
import datetime

# 🔥 아두이노 시리얼 포트 설정
PORT = "COM6"  # 💡 아두이노 연결된 포트 확인
BAUDRATE = 9600

# ✅ 시리얼 포트 전역 변수로 선언 (한 번만 열도록)
try:
    ser = serial.Serial(PORT, BAUDRATE, timeout=2)
    time.sleep(2)  # 아두이노 초기화 대기
    ser.flushInput()  # 기존 버퍼 삭제
except serial.SerialException as e:
    print(f"❌ 시리얼 포트 오류: {e}")
    ser = None  # 시리얼 포트 열기에 실패하면 None 설정

def get_sensor_data():
    """아두이노에서 온습도 및 PM2.5 데이터를 읽어오는 함수"""
    if ser is None:  # 포트가 제대로 열리지 않았으면 바로 리턴
        return "N/A", "N/A", "N/A"

    ser.flushInput()  # 🔥 버퍼 삭제 후 데이터 읽기
    start_time = time.time()  # 🔥 타임아웃 설정 (최대 5초 대기)

    while True:  
        if time.time() - start_time > 5:  # 5초 이상 기다렸다면 강제 종료
            print("⏳ 데이터 수신 타임아웃!")
            return "N/A", "N/A", "N/A"

        if ser.in_waiting:  # 시리얼 버퍼에 데이터가 있는 경우
            line = ser.readline().decode("utf-8").strip()
            if line:
                print(f"📡 Arduino Raw Data: {line}")  # 디버깅 출력
                data = line.split(",")

                if len(data) == 2:  # 온도, 습도만 받을 경우
                    return data[0], data[1], "N/A"

                elif len(data) == 3:  # 온도, 습도, PM2.5 값이 모두 있을 경우
                    return data[0], data[1], data[2]

                else:
                    print("⚠️ 잘못된 데이터 형식! 다시 읽는 중...")
                    continue  # 다시 읽기

# Flask 애플리케이션 생성
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    """Flask API: 아두이노 센서 데이터 제공"""
    temperature, humidity, pm25 = get_sensor_data()

    # 현재 시간 가져오기
    current_time = datetime.datetime.now().strftime('%H:%M:%S')

    # JSON 응답 생성
    data = {
        "temperature": temperature,
        "humidity": humidity,
        "pm25": pm25,
        "current_time": current_time
    }
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
