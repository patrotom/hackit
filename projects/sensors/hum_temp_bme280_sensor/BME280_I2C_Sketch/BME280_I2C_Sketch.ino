#include <Wire.h>
#include "cactus_io_BME280_I2C.h"
// http://cactus.io/hookups/sensors/barometric/bme280/hookup-arduino-to-bme280-barometric-pressure-sensor
//BME280_I2C bme;              // I2C using default 0x77 
BME280_I2C bme(0x76);  // I2C using address 0x76

void setup() {
  Serial.begin(9600);
  
  if (!bme.begin()) {
    Serial.println("Could not find a valid BME280 sensor, check wiring!");
    while (1);
  }

  bme.setTempCal(-1);
  
  Serial.println("Pressure\tHumdity\t\tTemp\t\tTemp");
  
}

void loop() {

    bme.readSensor(); 
  
    Serial.print(bme.getPressure_MB()); Serial.print("\t\t");    // Pressure in millibars
    Serial.print(bme.getHumidity()); Serial.print("\t\t");
    Serial.print(bme.getTemperature_C()); Serial.println(" *C\t");
    
    delay(500);
}
