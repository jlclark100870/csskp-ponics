#!/usr/bin/python3
import time
import datetime
import timer_script

while True:
    set_alarm_timer = f"{00}:{19}:{00}"
    off_alarm_set = f"{13}:{00}:{00}"
    timer_script.alarm(set_alarm_timer , off_alarm_set)
    time.sleep(30)
    

