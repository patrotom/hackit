#include <DHT.h>

#define DHTPIN D8
#define DHTTYPE DHT22 
 
DHT dht(DHTPIN, DHTTYPE);
 
void setup() 
{
    Serial.begin(115200);
    delay(10);
    dht.begin();
 
}
 
void loop() 
{
 
    float h = dht.readHumidity();
    float t = dht.readTemperature();
    if (isnan(h) || isnan(t)) 
    {
    Serial.println("Failed to read from DHT sensor!");
    return;
    }
    
    
        
        
        
        Serial.print("Temperature: ");
        Serial.print(t);
        Serial.print(" degrees Celsius Humidity: ");
        Serial.print(h);
        Serial.println("Sending data to Thingspeak");
    
   
    
    Serial.println("Waiting 20 secs");
    delay(4000);
}
