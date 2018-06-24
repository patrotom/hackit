/*  Connects to the home WiFi network
 *  Asks some network parameters
 *  Sends and receives message from the server in every 2 seconds
 *  Communicates: wifi_server_01.ino
 */ 

#include <DHT.h>
#include <SPI.h>
#include <ESP8266WiFi.h>
#define DHTPIN 8
#define DHTTYPE DHT22  

char ssid[] = "HackIT";           // SSID of your home WiFi
char pass[] = "SlovakiaForTheWin";            // password of your home WiFi
String text = "data k teplote a vlhkosti ";


DHT dht(DHTPIN, DHTTYPE);
IPAddress server(192,168,10,1);       // the fix IP address of the server
WiFiClient client;



void setup() {
  Serial.begin(115200);               // only for debug
  delay(1000);
  dht.begin();
  Serial.println("zapol sa serial");
  
  WiFi.begin(ssid, pass);             // connects to the WiFi router
  delay(1000);
  Serial.println("zapol som dht a wifi");
  delay(1000);
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

void loop () {
  float h = dht.readHumidity();
  delay(1000);
  float t = dht.readTemperature();
  delay(1000);
  
  if (isnan(t) || isnan(h)) 
    {
    Serial.println("Failed to read from DHT sensor!");
    }
  
  if(client.connect(server, 10000)){   // Connection to the server
    String postStr = text;
    postStr +="&field1=";
    postStr += String(t);
    postStr +="&field2=";
    postStr += String(h);
    postStr += "\r\n\r\n";

    client.print("Dlzka spravy: ");
    client.print(postStr.length());
    client.print("\n\n sprava: ");
    client.print(postStr);

    Serial.print("Temperature: ");
    Serial.print(t);
    Serial.print(" degrees Celsius,    Humidity: ");
    Serial.print(h);  

  }

  Serial.println(".");
  client.println("Matej straka kedy vychadza album?\r");  // sends the message to the server
  
  String answer = client.readStringUntil('\r');   // receives the answer from the sever
  Serial.println("from server: " + answer);
  client.flush();
  client.stop();
  
  delay(1000);                  // client will trigger the communication after two seconds
}



