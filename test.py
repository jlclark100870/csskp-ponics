## Adding hours or minutes or seconds to datetime
from datetime import datetime, timedelta
 
## Original datetime
datetime_original = datetime(year=2006, month=11, day=23)
print("\nOriginal date: ", datetime_original, "\n")
 
## Adding Hours
hours_to_add = 12
datetime_new = datetime_original + timedelta(hours = hours_to_add)
print("After adding hours: ", datetime_new, "\n")
 
## Adding Minutes
minutes_to_add = 45
datetime_new = datetime_new + timedelta(minutes = minutes_to_add)
print("After adding minutes: ", datetime_new, "\n")
 
## Adding Seconds
seconds_to_add = 33
datetime_new = datetime_new + timedelta(seconds = seconds_to_add)
print("After adding seconds: ", datetime_new, "\n")
 
## Adding Microseconds
microseconds_to_add = 12345
datetime_new = datetime_new + timedelta(microseconds = microseconds_to_add)
print("After adding microseconds: ", datetime_new, "\n")