void setup() {
  Serial.begin(9600); // 시리얼 통신 속도 설정
}

void loop() {
  int temp = random(20, 30);  // 임의의 온도 값 (20~30도)
  int hum = random(40, 60);   // 임의의 습도 값 (40~60%)

  Serial.print(temp);
  Serial.print(",");
  Serial.println(hum);

  delay(500); // 0.5초 대기
}
