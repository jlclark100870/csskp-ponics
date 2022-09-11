#!/usr/bin/python3
#importing the required modules
from datetime import datetime, timedelta
import datetime as dt
import time
import readjson
import relaytest
import var_check

def main():
    while True:
        heat()

def heat():
    tempset = var_check.checks("fan_temp_on")
    temp = var_check.checkd('air_temp')
    print(temp)

    if float(temp) < float(tempset):
        relaytest.tempon()
        heater_status = 'heater on'
    elif float(temp) >= float(tempset):
        relaytest.tempoff()
        heater_status = 'heater off'
    else:
        relaytest.tempoff()
        heater_status = 'heater off'

    return(heater_status)
        

    
def humid():
    humidset = var_check.checks("humidity")
    humid = var_check.checkd('humidity')
    print(humid)
   

    if float(humid) > float(humidset):
        relaytest.humidon()       
        humidity_status = "on"

    elif float(humid) <= float(humidset):
        relaytest.humidoff()       
        humidity_status = "off"
    else:
        relaytest.humidoff()       
        humidity_status = "off"

    return(humidity_status)

if __name__ == "__main__":
    main()