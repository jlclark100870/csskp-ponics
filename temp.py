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
        print("on")
    if float(temp) > float(tempset):
        relaytest.tempoff()
        print("off")

    time.sleep(30)



if __name__ == "__main__":
    main()