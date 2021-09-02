#!/usr/bin/python3
import sys
import readjson
import relaytest

relaytest.main()

import requests
import serial
from time import sleep, time
import json
import i2c
import datetime
import schedule
import var_check
import datetime
import timer_script
from imagecap import imcap
import logging
import poniclog

ph_timer1 = 0

schedule.every(4).hours.do(imcap)

#def checks(set_name):
    
    #p1 = readjson.contsets(set_name)
    #ph_clock = p1.myfunc()
    #return ph_clock

def light_cont():
    global status
    status = timer_script.alarm()
    	

def timer_func():

    var_check.ph_check()
    var_check.ec_check()
    
def timer_ph(ph_timer):
    
    print(ph_timer)
    global ph_timer1
    if ph_timer != ph_timer1:
        schedule.clear()
        schedule.every(ph_timer).minutes.do(timer_func)
        schedule.every(4).hours.do(imcap)
        ph_timer1 = ph_timer




        
######################################setting url values

try:

    ser = serial.Serial("/dev/ttyUSB0", 9600)
    url = 'http://csskp.com/api/v1/machines/test.php'

except:

    
    logging.error('fuck', exc_info=True)
##################################################end setting url values





while True:


    light_cont()
    
    ser.reset_input_buffer()
    seq=[]
    timeout = time() + 5   # 5 minutes from now
    while time() < timeout:
        try:
   
            schedule.run_pending()


            tdt= time()
            data = ser.readline()
    
            data = data.decode().strip('\r\n')
            rawData = data.split(',')

            data = {                        
                        'humidity' : float(rawData[1]),
                        'air_temp' : float(rawData[2]),
                        'lightSensor' : int(rawData[3]),
                        'water_temp' : float(rawData[4]),
                        'time' : tdt,
                        'PH' : float(i2c.phread()),
			'EC' : float(i2c.ecread()),
                        'grow_light' : status
                        }

            myobj = json.dumps(data)
                    

            x = requests.post(url, myobj)

            #print the response text (the content of the requested file):
            print(myobj)
            logging.info(myobj)        
                    
            timer_ph(var_check.checks('ph_test_time'))
            sleep(10)  

        except:
            seq=[]
           
            print("Waiting for data")
            print("Unexpected error:", sys.exc_info()[1])
            logging.error('Exception occured', exc_info=True)
