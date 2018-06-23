int FlamePin = 0;  // This is for input pin
int Flame = 0;

void setup() {
  pinMode(A0, INPUT);
  Serial.begin(9600);
  
}

void loop() {
  Flame = analogRead(FlamePin);
  delay(500);
  if (Flame < 15)
  {
    Serial.println("HIGH FLAME");
    Serial.println(Flame);
  }
  else
  {
    Serial.println("No flame");
    Serial.println(Flame);
  }
}

