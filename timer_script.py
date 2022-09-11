#!/usr/bin/python3

from datetime import *
import time
import readjson
import relaytest

def main():

    while True:

        print(alarm())
        time.sleep(10)


def checks(set_name):
    p1 = readjson.contsets(set_name)
    myfunc_results = p1.myfunc()
    return myfunc_results


def alarm():

    lighton_var = checks('daylength')
    alarm_var = checks('daycycle')
    alarm_hour = int(alarm_var[0:2])
    alarm_minute = int(alarm_var[4:5])
    current_time = datetime.now()
    
    lighton_time = datetime.strptime(lighton_var, '%H:%M:%S')
    lighton_time = lighton_time.replace(year=current_time.year, month=current_time.month, day=current_time.day)
    alarm_time = datetime.strptime(alarm_var, '%H:%M:%S')
    alarm_time = alarm_time.replace(year=current_time.year, month=current_time.month, day=current_time.day)
    
    

    if current_time > alarm_time :
        status = "off"
        relaytest.lightoff()
    elif  current_time < alarm_time and current_time > lighton_time:
        status = "on"
        relaytest.lighton()
    elif current_time < alarm_time and current_time < lighton_time:
        status = 'off'
        relaytest.lightoff()
    else:
        status = "unassigned"
    

   
    return (status)

if __name__ == "__main__":
         main()