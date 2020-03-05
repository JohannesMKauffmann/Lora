#include <dht.h>
#define DHT11_PIN 3
dht DHT;

void setup()
{         
  Serial.begin(115200);
}

void loop(){
 DHT.read11(DHT11_PIN);
 String data = String(DHT.humidity, 1) + ',' + String(DHT.temperature, 1);
 Serial.println(data);
 delay(2000);
}
