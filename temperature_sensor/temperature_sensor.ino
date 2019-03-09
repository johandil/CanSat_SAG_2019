// tutorial: http://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-an-arduino/
#include <dht.h>
using namespace std;
dht DHT;

int DHT11_PIN = 7;

void setup(){
  Serial.begin(9600);
  
}

void loop()
{
  DHT.read11(DHT11_PIN); //read data
  Serial.print(DHT.temperature); //print temperature
  Serial.print(", ");
  Serial.println(DHT.humidity); //print humidity
  delay(1100);
  
}
