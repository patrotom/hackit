#include <SPI.h>
#include <ESP8266WiFi.h>

char ssid[] = "HackIT";           // SSID of your home WiFi
char pass[] = "SlovakiaForTheWin";            // password of your home WiFi
String data = "";
IPAddress server(192,168,10,1);       // the fix IP address of the server
WiFiClient client;


void setup() {
  Serial.begin(115200);
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

void loop() {
  if(Serial.available()>0){
    data = Serial.readString(); //Read the serial data and store in var
    Serial.println(data); //Print data on Serial Monitor
    delay(500);
  }

  if(client.connect(server, 10000)){   // Connection to the server
    client.println(data);
    
    String answer = client.readStringUntil('\r');   // receives the answer from the sever
    //Serial.println("from server: " + answer);
    Serial.println(answer);
    if (answer == "1"){
      Serial.println("1");
    }
    else if (answer == "2"){
      Serial.println("2");
    }
    
    client.flush();
    client.stop(); 
    delay(500);
  }
  
  delay(2000);
}
