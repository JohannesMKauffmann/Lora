#include <dht.h>
#define DHT11_PIN 2
dht DHT;

void setup()
{         
  Serial.begin(9600);
}

void loop(){
 Serial.print("DHT11, \t");
 int chk = DHT.read11(DHT11_PIN);
 Serial.print((DHT.humidity), 1);
 Serial.print(",\t\t");
 Serial.println((DHT.temperature), 1);

 delay(2000);
}
