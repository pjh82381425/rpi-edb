import serial

PORT = "COM6"  # 🔥 올바른 포트로 변경하세요.
BAUDRATE = 9600

ser = serial.Serial(PORT, BAUDRATE, timeout=2)  # timeout 증가

def read():
    ser.flushInput()  # 🔥 기존 버퍼 삭제
    latest_temp, latest_hum = None, None
    while ser.in_waiting == None:
        pass
    line = ser.readline().decode("utf-8").strip()
    if line:
        data = line.split(",")
        if len(data) == 2:
            latest_temp, latest_hum = data  # 최신 값 저장
    
    ser.close()  # 🔥 포트 닫기
    return latest_temp, latest_hum

print("읽기 시도")
data = read()
print(f"{data}")