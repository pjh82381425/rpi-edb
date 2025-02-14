#include <dht11.h>
#define DHT11PIN 2

dht11 DHT11;

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  int chk = DHT11.read(DHT11PIN);
  Serial.print((int)DHT11.humidity);
  Serial.print(",");
  Serial.print((int)DHT11.temperature);
  Serial.println();
  delay(250);
}