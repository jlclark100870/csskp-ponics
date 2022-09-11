#!/usr/bin/python3
from ast import IsNot, Not
from bdb import Breakpoint
import poniclog
import logging
import timer_script
import var_check
import schedule
import datetime
import json
from time import sleep, time
import serial
import requests
import temp
import sys
import readjson
import relaytest
from datetime import datetime





    
        


    
relaytest.main()
# import i2c
# from imagecap import imcap
#set global varibal for ph_timer1 to 0
ph_timer1 = 0
url = 'http://csskp.com/api/v1/machines/test.php'
#set scedule for taking pictures of inside cabinet
# schedule.every(4).hours.do(imcap)


def light_status():
    #check wether light is to be on or off
    status = timer_script.alarm()
    return(status)

def hum_status():
    status = temp.humid()
    return (status)

def timer_func():
    #chek ph and ec values
    var_check.ph_check()
    var_check.ec_check()


def timer_ph(ph_timer):
    #set timer for when to check ph and ec levels and set timer for json write to website
    print(ph_timer)
    global ph_timer1
    if ph_timer != ph_timer1:
        schedule.clear()
        schedule.every(ph_timer).minutes.do(timer_func)
        schedule.every(5).minutes.do(write_week1)
        # schedule.every(4).hours.do(imcap)
        ph_timer1 = ph_timer





def output():
       
    
    try:
       
        nowstr = str(datetime.now())
        ser = serial.Serial("/dev/ttyUSB0", 9600)
        ser.reset_input_buffer()  
        
        #check temp and heater status
        temp.heat()
        heaterstatus = temp.heat()
        lightstatus = light_status()
        humidstatus = hum_status()
        tdt = time()
        data = ser.readline()

        data = data.decode().strip('\r\n')
        rawData = data.split(',')

        data = {
            'growtime': float(var_check.checkg('plantdate')),
            'humidity': float(rawData[1]),
            'air_temp': float(rawData[2]),
            'lightSensor': int(rawData[3]),
            'water_temp': float(rawData[4]),
            'time': tdt,
            'PH': float(7),
            'EC': float(1.6),
            'grow_light': lightstatus,
            'heater_status': heaterstatus,
            'humidifier_status': humidstatus
        }

        myobj = json.dumps(data)
        logging.info(nowstr)
        logging.info(myobj)

        ser.close
   # except:
    #    report = "_________________________________________That's not a number. Please try again._______________________________________________"
     #   print("read myObj Unexpected error:", sys.exc_info()[1])
      #  print(report)
       # logging.info(report)
    except:
        print("output connection failed")
        print("read myObj Unexpected error:", sys.exc_info()[1])
        logging.error('Exception occured', exc_info=True)
        sleep(30)
   

    return(myobj)

def write_locally():
    try:
        nowstr = str(datetime.now())
        myobj = output()
        if myobj != None:
            
            f = open("/home/pi/Desktop/myponic/details.json", "w")
            f.write(myobj)
            report ='___________________wrote locally to details.json_____________________________________________________'
            print(report)
            logging.info(report)
            f.close()
        else:
            myobj = output()
    except:
        print("write_details connection failed")
        print("write myObj Unexpected error:", sys.exc_info()[1])
        logging.error('Exception occured', exc_info=True)
        sleep(30)

def write_week1():
    try:
        nowstr = str(datetime.now())
        myobj = output()
        if myobj != None:
       
            x = requests.post(url, myobj, timeout=10)

            # print the response text (the content of the requested file):
            print(myobj)
            logging.info(myobj)
            report = '________________________wrote data to json file_____________________________________________________________'
            print(report)
            logging.info(report)
        
        else:
            myobj = output()
            
    except:
        print("write_week1 connection failed")
        print("write myObj Unexpected error:", sys.exc_info()[1])
        logging.error('Exception occured', exc_info=True)
        sleep(30)

       
write_week1()
ph_timer=var_check.checks('ph_test_time')
print(ph_timer,' minutes to json write')
timer_ph(ph_timer)
while True:
    nowstr = str(datetime.now())
    sleep(1)
    write_locally()
    print(nowstr)
    sleep(60)
    schedule.run_pending()
    

    
