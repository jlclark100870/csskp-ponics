## Adding hours or minutes or seconds to datetime
import time
import datetime
import readjson
from datetime import timedelta


def checks(set_name):
    p1 = readjson.contsets(set_name)
    myfunc_results = p1.myfunc()
    return myfunc_results
 
def time_list():
    dt = list(time.localtime())
    month = dt[1]
    day = dt[2]
    year = dt[0]
    hour = dt[3]
    minute = dt[4]
    second = dt[5]
    
    now = datetime.time()
    current_time = now.strftime("%H:%M:%S")
    
    now_time = now
    day_length = int(checks('daylength'))
    alarm_time = checks('daycycle')
    alarm_hour=int(alarm_time[0:2])
    alarm_minute=int(alarm_time[3:5])
    alarm_second=int(alarm_time[6:8])
    
    
time1= datetime.time(alarm_hour,alarm_minute,alarm_second)
    

  
print(time1)
print (now_time)
if time1 > now_time:
    print ('wake up')
        
        
    