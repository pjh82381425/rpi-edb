import serial

def read():
    PORT = "/dev/ttyACM0"  # 🔥 올바른 포트로 변경
    BAUDRATE = 9600
    ser = serial.Serial(PORT, BAUDRATE, timeout=2)  # timeout 증가
    ser.flushInput()  # 🔥 기존 버퍼 삭제
    latest_temp, latest_hum, latest_pm25 = None, None, None
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode("utf-8").strip()
            if line:
                data = line.split(",")
                if len(data) == 3:
                    latest_temp, latest_hum, latest_pm25 = data  # 최신 값 저장
                    break
    ser.close()  # 🔥 포트 닫기
    return latest_temp, latest_hum, latest_pm25

a = read()
print(a)