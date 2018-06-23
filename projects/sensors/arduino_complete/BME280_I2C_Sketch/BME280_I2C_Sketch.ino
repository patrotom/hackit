#include <Wire.h>
#include "cactus_io_BME280_I2C.h"
#include <Servo.h>

const int flamable_sensor_pin = A0;
const int co_sensor_pin = A1;
const int servo_pin = A2;

const int servo_initial_position = 90;
const int servo_final_position = 180;
int servo_position = servo_initial_position;

int pressure = 0;
int humidity = 0;
int temperature = 0;
int flamable_ratio = 0;
int co_ppm = 0;

BME280_I2C bme(0x76);  // I2C using address 0x76
Servo servo_motor; 

void setup() {
  Serial.begin(9600);
  
  if (!bme.begin()) {
    Serial.println("Could not find a valid BME280 sensor, check wiring!");
    while (1);
  }
  bme.setTempCal(-1);
  
  servo_motor.attach(servo_pin);
  servo_motor.write(servo_initial_position);
  
  
}

void loop() {
    bme.readSensor(); 
    pressure = bme.getPressure_MB();
    humidity = bme.getHumidity();
    temperature = bme.getTemperature_C();
    flamable_ratio = map(analogRead(flamable_sensor_pin), 0, 1023, 0, 100);
    co_ppm = map(((((5.0 - ((float)analogRead(co_sensor_pin) / 1024 * 5.0)) / ((float)analogRead(co_sensor_pin) / 1024 * 5.0)) / 1.62 )* 100), 150, 79, 200, 1000);
  
    Serial.print(pressure); Serial.print("hPa\t\t");    // Pressure in millibars
    Serial.print(humidity); Serial.print("hum\t\t");
    Serial.print(temperature); Serial.print("*C\t\t");
    Serial.print(flamable_ratio); Serial.print("per\t\t");
    Serial.print(co_ppm); Serial.println("ppm\t");
    
    if ( Serial.available()) {
      char ch = Serial.read();
  
      if(ch == '1') {
        for(servo_position; servo_position <= servo_final_position; servo_position++){
          servo_motor.write(servo_position);
          delay(20);
        }
      }
      
      if(ch == '0') {
        for(servo_position; servo_position >= servo_initial_position; servo_position--){
          servo_motor.write(servo_position);
          delay(20);
        }
      }
      
  }
    
    delay(500);
}
