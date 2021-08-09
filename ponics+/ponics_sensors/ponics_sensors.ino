#include <OneWire.h>
#include <DallasTemperature.h>
#include <DHT.h>

//Constants
#define ONE_WIRE_BUS 2
#define DHTPIN 7     // what pin we're connected to
#define DHTTYPE DHT22   // DHT 22  (AM2302)
const int LDR = A2;
DHT dht(DHTPIN, DHTTYPE); //// Initialize DHT sensor for normal 16mhz Arduino
// Data wire is plugged into pin 2 on the Arduino

// Setup a oneWire instance to communicate with any OneWire devices 
// (not just Maxim/Dallas temperature ICs)
OneWire oneWire(ONE_WIRE_BUS);

 
// Pass our oneWire reference to Dallas Temperature.
DallasTemperature sensors(&oneWire);
 
//Variables
int chk;
float hum;  //Stores humidity value
float temp; //Stores temperature value


int input_val = 0;

void setup()
{
  Serial.begin(9600);
  dht.begin();
   // Start up the library
  sensors.begin();
}

void loop()
{
    delay(1500);
    //Read data and store it to variables hum and temp
    hum = dht.readHumidity();
    temp= dht.readTemperature();
     input_val = analogRead(LDR);
    sensors.requestTemperatures(); // Send the command to get temperatures

    
    //Print temp and humidity values to serial monitor
    Serial.print("#,");
    Serial.print(hum);
    Serial.print(",");
    Serial.print(temp);
    Serial.print(",");
    Serial.print(input_val);
    Serial.print(",");
    Serial.println(sensors.getTempCByIndex(0)); // Why "byIndex"
    //Serial.print(",");
    //delay(2000); //Delay 2 sec.
}

   
