#include "DHT.h"
#define pinDHT D8
#define typDHT22 DHT22   // DHT 22 (AM2302)
#include <SPI.h>
#include <ESP8266WiFi.h>

char ssid[] = "HackIT";           // SSID of your home WiFi
char pass[] = "SlovakiaForTheWin";            // password of your home WiFi
String data = "";
IPAddress server(192,168,10,1);       // the fix IP address of the server
WiFiClient client;
DHT mojeDHT(pinDHT, typDHT22);

void setup() {
  Serial.begin(115200); 
  delay(10);
  mojeDHT.begin();
  Serial.println("zapol sa serial a dht");
  delay(20);
  WiFi.begin(ssid, pass);             // connects to the WiFi router
  delay(200);
  Serial.println("zapol som wifi");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  Serial.println("Connected to wifi");
  Serial.print("Status: ");  Serial.println(WiFi.status());    // Network parameters
  Serial.print("IP: ");      Serial.println(WiFi.localIP());
  Serial.print("Subnet: ");  Serial.println(WiFi.subnetMask());
  Serial.print("Gateway: "); Serial.println(WiFi.gatewayIP());
  Serial.print("SSID: ");    Serial.println(WiFi.SSID());
  Serial.print("Signal: ");  Serial.println(WiFi.RSSI());

}

void loop() {
  int temperature = mojeDHT.readTemperature();
  int humidity = mojeDHT.readHumidity();
  String message3 = String(3) + "|" + String(temperature) + "|" + String(humidity) + "|" + "0" + "|" + "0";

 

  if(client.connect(server, 10000)){   // Connection to the server
    client.println(message3);
    client.flush();
    client.stop(); 
    delay(500);
  }
  
  delay(2000);
}
