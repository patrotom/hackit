int buzzer = 8;
int led = 7;
int smokeA0 = A5;

void setup() {
  pinMode(buzzer, OUTPUT);
  pinMode(smokeA0, INPUT);
  pinMode(led, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  float sensor_volt;
  float sensorValue;
 
  sensorValue = analogRead(smokeA0);
  sensor_volt = sensorValue/1024*5.0; //ked je viac ako 0,9V ->hori
 
  Serial.print("sensor_volt = ");
  Serial.print(sensor_volt);
  Serial.println("V");
    
  if (sensor_volt > 0.9)
  {
    Serial.println("hori"); //hori
    digitalWrite(led, HIGH);
    for(int i = 0; i< 500;i++){
      digitalWrite(buzzer,HIGH);
      delay(1);//wait for 1ms
      digitalWrite(buzzer,LOW);
      delay(1);//wait for 1ms
    }
    
  }
  else
  {
    digitalWrite(led, LOW); 
  }
  delay(1000);
}
