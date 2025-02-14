#include <dht11.h>
#include <SoftwareSerial.h> 
#define DHT11PIN 2

dht11 DHT11;
SoftwareSerial HC12(2, 3); // 아두이노 2번을 HC-12 TX Pin에 연결, 3번을 HC-12 RX Pin에 연결.

void setup()
{
  Serial.begin(9600);
  HC12.begin(9600);   // 시리얼포트(아두이노) ↔ HC12 통신속도(bps)
}

void loop()
{
  while (HC12.available()) {
    String input = HC12.readStringUntil('\n');
    Serial.print(input);
    Serial.print(",");
    int chk = DHT11.read(DHT11PIN);
    Serial.print((int)DHT11.humidity);
    Serial.print(",");
    Serial.print((int)DHT11.temperature);
    Serial.println();
    delay(10);
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
