import serial
import time

PORT = "COM6"  # 🔥 올바른 포트로 변경하세요.
BAUDRATE = 9600

ser = serial.Serial(PORT, BAUDRATE, timeout=2)  # timeout 증가
time.sleep(2)  # 🔥 아두이노 초기화 대기
ser.flushInput()  # 🔥 기존 버퍼 삭제

def read():
    latest_temp, latest_hum = None, None
    
    for _ in range(5):  # 🔥 여러 번 읽고 최신 값 저장
        if ser.in_waiting:  # 데이터가 있는 경우
            line = ser.readline().decode("utf-8").strip()
            print(f"📡 Raw Data: {line}")  # 🔥 디버깅용 출력
            if line:
                data = line.split(",")
                if len(data) == 2:
                    latest_temp, latest_hum = data  # 최신 값 저장
                    break  # 첫 번째 정상 값 읽고 종료
    
    ser.close()  # 🔥 포트 닫기
    return latest_temp, latest_hum

temp, hum = read()

if temp and hum:
    print(f"📌 최종 Temperature: {temp}")
    print(f"📌 최종 Humidity: {hum}")
else:
    print("❌ 데이터를 읽지 못했습니다. 아두이노가 올바른 데이터를 보내고 있는지 확인하세요.")

def get_pm25():
    return 1