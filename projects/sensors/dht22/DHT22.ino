// Teploměr a vlhkoměr DHT11/22

#include "DHT.h"  // připojení knihovny DHT
#define pinDHT 8  // nastavení čísla pinu s připojeným DHT senzorem
#define typDHT22 DHT22   // DHT 22 (AM2302)

// inicializace DHT senzoru s nastaveným pinem a typem senzoru
DHT mojeDHT(pinDHT, typDHT22);

void setup() {
  Serial.begin(9600); // komunikace přes sériovou linku rychlostí 9600 baud
  mojeDHT.begin();    // zapnutí komunikace s teploměrem DHT
}

void loop() {
  // pomocí funkcí readTemperature a readHumidity načteme
  // do proměnných tep a vlh informace o teplotě a vlhkosti,
  // čtení trvá cca 250 ms
  float tep = mojeDHT.readTemperature();
  float vlh = mojeDHT.readHumidity();
  // kontrola, jestli jsou načtené hodnoty čísla pomocí funkce isnan
  if (isnan(tep) || isnan(vlh)) {
    Serial.println("Chyba při čtení z DHT senzoru!"); // při chybném čtení vypiš hlášku
  } else {
    Serial.print("Teplota: "); 
    Serial.print(tep);
    Serial.print(" stupnov Celsia, ");
    Serial.print("vlhkost: "); 
    Serial.print(vlh);
    Serial.println("  %");
  }
  delay(2000);// pauza pro přehlednější výpis
}
