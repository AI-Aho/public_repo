#include<dht.h>
dht DHT
const int dhtPin = 2;
float temperature = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int check = DHT.read11(dhtPin);
  Serial.print("Temperature:");
  temperature = DHT.temperature;
  Serial.println(temperature);
  Serial.print("Humidity");
  Serial.println(DHT.humidity);
  delay(1000);
  
}
