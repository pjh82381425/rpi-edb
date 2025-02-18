#include <dht11.h>
#include <SoftwareSerial.h> 
#define DHT11PIN 2

dht11 DHT11;
SoftwareSerial HC12(3, 4); // 아두이노 2번을 HC-12 TX Pin에 연결, 3번을 HC-12 RX Pin에 연결.
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
  if (HC12.available()) {
    int chk = DHT11.read(DHT11PIN);
    Serial.print((int)DHT11.temperature);
    Serial.print(",");
    Serial.print((int)DHT11.humidity);
    Serial.print(",");
    String input = HC12.readStringUntil('\n');
    Serial.print(input);
    Serial.println();
    delay(250);
  }
  else {
    int chk = DHT11.read(DHT11PIN);
    Serial.print((int)DHT11.temperature);
    Serial.print(",");
    Serial.print((int)DHT11.humidity);
    Serial.print(",N/A");
    Serial.println();
    delay(250);
  }
}

// void loop() { 
//   // // 시리얼모니터로 수신(입력)데이터가 있을 경우 HC12를 통해 데이터를 발송  
//   // while (Serial.available()) { 
//   //   String input = Serial.readString();
//   //   HC12.println(input);
//   // } 
//   // HC12모듈이 받은 데이터가 있을 경우 시리얼모니터로 출력
//   while (HC12.available()) { 
//     String input = HC12.readStringUntil('\n');
//     Serial.print(input);
//   } 
//   delay (20);
// }
