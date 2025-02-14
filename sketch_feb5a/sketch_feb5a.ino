#include <dht11.h>
#include <SoftwareSerial.h> 
#define DHT11PIN 2
#define hc12SetPin 5 // HC-12 SET 핀을 아두이노의 7번 핀에 연결

dht11 DHT11;
SoftwareSerial HC12(3, 4); // 아두이노 2번을 HC-12 TX Pin에 연결, 3번을 HC-12 RX Pin에 연결.

void setATCommandMode(bool mode) {
  digitalWrite(hc12SetPin, mode ? LOW : HIGH); // pull SET to LOW to activate AT command mode
  delay(mode ? 40 : 80); // according to doc (40ms upon activation, 80ms upon exit)
}

void setup()
{
  pinMode(hc12SetPin, OUTPUT);
  Serial.begin(9600);
  HC12.begin(9600);   // 시리얼포트(아두이노) ↔ HC12 통신속도(bps)

  // AT 명령 모드로 전환
  setATCommandMode(true);
  HC12.print("AT+C050"); // 채널 50으로 설정
  delay(100);
  setATCommandMode(false);
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
    Serial.print(",NULL");
    Serial.println();
    delay(250);
  }
}
