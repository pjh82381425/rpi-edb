// ###  'AT-Command'  실습     ###
// HC12 모듈의 Setup Pin을 활용한 HC12의 채널/속도/모드... 변경 실습 
// HC12모듈을 연결한 회로를 준비합니다 (아래 링크 참조)
// RasINO IoT : https://rasino.tistory.com/326
// AT+Cxxx
// 433.4MHz + (CH번호 - 1) × 0.4MHz 로 계산

#include <SoftwareSerial.h>
SoftwareSerial HC12(3, 4);
#define setPin 5  // HC12 모듈의 SET 핀에 연결될 아두이노 핀 번호 정의 함

void setup() 
{
  Serial.begin(9600);
  HC12.begin(9600);
  pinMode(setPin,OUTPUT);
  digitalWrite(setPin,LOW);  //  AT command mode 진입
  delay(100);                // 명령어 전달되는 시간을 기다려 줌 
  HC12.write("AT");          // AT 명령어 입력 ( "OK" 문자 응답)
  delay(300);                // 명령어 전달되는 시간을 기다려 줌 
  HC12.write("AT+C095\r\n"); // 채널 설정 (471.4MHz)
  delay(300);                // 명령어 전달되는 시간을 기다려 줌   
  HC12.write("AT+RX\r\n");
  delay(300);                // 명령어 전달되는 시간을 기다려 줌   
  digitalWrite(setPin,HIGH); // AT-mode 빠져나옴(data 전송모드)
}

void loop() 
{ 
  HC12.println("10");
  // 센서 값 읽는 로직 필요
}