#!/usr/bin/python3
import time
import datetime
import readjson
import relaytest


def checks(set_name):
    p1 = readjson.contsets(set_name)
    myfunc_results = p1.myfunc()
    return myfunc_results

def alarm():
    
    day_length = checks('daylength')
    on_hour= day_length[0:2]
    on_minute= day_length[3:5]
    alarm_time = checks('daycycle')
    alarm_hour= alarm_time[0:2]
    alarm_minute= alarm_time[3:5]
    light_on =f"{on_hour}:{on_minute}:{'00'}"
    off_alarm_timer =  f"{alarm_hour}:{alarm_minute}:{'00'}"
    time.sleep(1)
    current_time = datetime.datetime.now()
    now = current_time.strftime("%H:%M:%S")
    date = current_time.strftime("%d/%m/%Y")
    #print("The Set Time is:",set_alarm_timer)
    #print(now)
    
    if now > light_on and now < off_alarm_timer:
        status = "Grow Light on"
        relaytest.lighton()
    elif now > off_alarm_timer:
        status = "Grow Light off"
        relaytest.lightoff()
    elif now > off_alarm_timer and now < light_on:
        status = "Grow Light off" 
        relaytest.lightoff()     
    else:
        status = "Grow Light off"
        relaytest.lightoff()

        
    return (status)

