#include <OneWire.h>
#include <DallasTemperature.h>
 
// Data wire is plugged into pin 2 on the Arduino
#define ONE_WIRE_BUS 12
#define SensorPin A0
float temp = 0;
// Setup a oneWire instance to communicate with any OneWire devices 
// (not just Maxim/Dallas temperature ICs)
OneWire oneWire(ONE_WIRE_BUS);
 
// Pass our oneWire reference to Dallas Temperature.
DallasTemperature sensors(&oneWire);

unsigned long previousMillis1 = 0;        // will store last time LED was updated
long hold = 4000;   

float sensorValue = 0; 
void setup(void)
{
  
  // start serial port
  Serial.begin(9600);
  

  // Start up the library
  sensors.begin();
}
 
 
void loop(void)
{

   unsigned long currentMillis = millis();
 //ds18B20 code in f
  
   
  if((currentMillis - previousMillis1 >= hold))
  {
    sensors.requestTemperatures(); // Send the command to get temperatures
    temp=sensors.getTempCByIndex(0);
    
    sensorValue = analogRead(SensorPin); 
    Serial.print(sensorValue);
    Serial.print(","); 
    Serial.print((temp*9/5)+32); // Why "byIndex"? 
    
    previousMillis1 = currentMillis;  // Remember the time
  }
  
    
}
