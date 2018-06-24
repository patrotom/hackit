/*  Connects to the home WiFi network
 *  Asks some network parameters
 *  Sends and receives message from the server in every 2 seconds
 *  Communicates: wifi_server_01.ino
 */ 


#include <SPI.h>
#include <ESP8266WiFi.h>


char ssid[] = "HackIT";           // SSID of your home WiFi
char pass[] = "SlovakiaForTheWin";            // password of your home WiFi
String text = "data k teplote a vlhkosti ";


IPAddress server(192,168,10,1);       // the fix IP address of the server
WiFiClient client;



void setup() {
  Serial.begin(115200);               // only for debug
  delay(20);
  Serial.println("zapol sa serial");
  
  WiFi.begin(ssid, pass);             // connects to the WiFi router
  delay(200);
  Serial.println("zapol som wifi");
  delay(200);
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
  
  if(client.connect(server, 10000)){   // Connection to the server
  

     

  

  Serial.println(".");
  client.println("Matej straka kedy vychadza album?\r");  // sends the message to the server
  
  String answer = client.readStringUntil('\r');   // receives the answer from the sever
  Serial.println("from server: " + answer);
  client.flush();
  client.stop();
  
  delay(1000);                  // client will trigger the communication after two seconds
}
}


