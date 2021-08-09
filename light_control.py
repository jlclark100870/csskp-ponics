#!/usr/bin/python3
#importing the required modules
from datetime import datetime, timedelta
import datetime as dt
import time
import readjson

def checks(set_name):
    p1 = readjson.contsets(set_name)
    myfunc_results = p1.myfunc()
    return myfunc_results



j=0


while j==0:
    
#obtaining the set time
    day_length = checks('daylength')
    alarm_time = checks('daycycle')
    alarm_hour=int(alarm_time[0:2])
    alarm_minute=int(alarm_time[3:5])

    
#obtaining the current time
    now = dt.datetime.now()
    current_hour = now.hour
    current_minute = now.minute
    print (current_hour,':',current_minute)
    print (alarm_hour,':',alarm_minute)
#obtaining the hour, minute, second and period of the current time
    
    if(alarm_hour==current_hour and alarm_minute < current_minute):
        day_period = alarm_hour + day_length
        if (day_period > 24):
            day_period = day_period - 24
        print("Light turns off at ", day_period, ':', alarm_minute,' hours')
       
        if (day_period == current_hour and alarm_minute < current_minute ):
            print('turning light off')
    
    time.sleep(60)