#include <Servo.h>

Servo servo_engine; 


void setup() {

  pinMode(1,OUTPUT);
  servo_engine.attach(14); //analog pin 0
  //servo1.setMaximumPulse(2000);
  //servo1.setMinimumPulse(700);

  Serial.begin(9600);
  Serial.println("Ready");

}

void loop() {
  static int const_of_movement = 5;
  static int move_servo = 90;
  servo_engine.write(move_servo);
  
  if ( Serial.available()) {
    char ch = Serial.read();

    if(ch == '1') {
      move_servo += const_of_movement;
      if(move_servo > 180){
        move_servo -= const_of_movement;
      }
      servo_engine.write(move_servo);
      Serial.println(move_servo);
    }
    
    if(ch == '2') {
      move_servo -= const_of_movement;
      if(move_servo < 0){
        move_servo += const_of_movement;
      }
      servo_engine.write(move_servo);
      Serial.println(move_servo);
    }
    
  }

} 
