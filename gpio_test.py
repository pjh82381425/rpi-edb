from machine import Pin, PWM
import time

# RGB LED에 연결된 GPIO 핀 설정
red = PWM(Pin(3)) #내가 연결한 것으로 변경 필요
green = PWM(Pin(4)) #내가 연결한 것으로 변경 필요
blue = PWM(Pin(5)) #내가 연결한 것으로 변경 필요

# PWM 주파수 설정
red.freq(1000)
green.freq(1000)
blue.freq(1000)

# 색상을 조정하는 함수
def set_color(r, g, b):
    red.duty_u16(r)
    green.duty_u16(g)
    blue.duty_u16(b)

# 주요 색상 사이를 부드럽게 전환
while True:
    # 빨간색에서 파란색으로 전환
    for i in range(0, 65535, 1000):
        set_color(65535-i, 0, i)
        time.sleep(0.01)
        
    # 파란색에서 초록색으로 전환
    for i in range(0, 65535, 1000):
        set_color(0, i, 65535-i)
        time.sleep(0.01)
        
    # 초록색에서 빨간색으로 전환
    for i in range(0, 65535, 1000):
        set_color(i, 65535-i, 0)
        time.sleep(0.01)