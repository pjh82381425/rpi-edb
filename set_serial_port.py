import serial

print("닫을 시리얼포트 번호 입력:")
c = input()

COM = f"COM{c}"
print(COM,"닫기 시도")

try:
    ser = serial.Serial("COM6", 9600, timeout=1)
    ser.close()  # 강제로 포트 닫기
    print(f"{COM} 시리얼 포트를 닫았습니다.")
except serial.SerialException as e:
    print(f"시리얼 포트 닫기 실패: {e}")
