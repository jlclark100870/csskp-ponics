#!/usr/bin/python3
import sys
import readjson
import relaytest
import RPi.GPIO as GPIO
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



relaytest.ecuon()
relaytest.phdon()
ph_timer1 = 0

schedule.every(4).hours.do(imcap)

def checks(set_name):
    
    p1 = readjson.contsets(set_name)
    ph_clock = p1.myfunc()
    return ph_clock

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

        
#sleep(20)




ser = serial.Serial("/dev/ttyACM0", 9600, timeout=0)
url = 'http://csskp.com/api/v1/machines/test.php'



while True:
    
    light_cont()
    ser.reset_input_buffer()
    seq=[]
    timeout = time() + 5   # 5 minutes from now
    while time() < timeout:
        try:
            
            schedule.run_pending() 
            for c in ser.read():
                seq.append(chr(c)) #convert from ANSII
                if chr(c) == '#':
                    now=datetime.datetime.now()                 
                    tdt= time()
                    joined_seq = ''.join(str(v) for v in seq) #Make a string from array
                    rawData = joined_seq[1:-1].split(',')
                    
                    data = {                        
                        'humidity' : float(rawData[0]),
                        'air_temp' : float(rawData[1]),
                        'lightSensor' : int(rawData[2]),
                        'water_temp' : float(rawData[3]),
                        'time' : tdt,
                        'PH' : float(i2c.phread()),
			'EC' : float(i2c.ecread()),
                        'grow_light' : status
                        }
                                        
                    

                    myobj = json.dumps(data)
                    

                    x = requests.post(url, myobj)

                    #print the response text (the content of the requested file):
                    print(myobj)
                    
                    
                    timer_ph(var_check.checks('ph_test_time'))
                    sleep(30)  
        except:
            seq=[]
           
            print("Waiting for data")
            print("Unexpected error:", sys.exc_info()[1])



                
    