import time
import sys
import readjson
import relaytest
#import schedule
import RPi.GPIO as GPIO

#---------------air temp fan control----------------------------

def main():
    val_check()

def checkd(set_name):
    p1 = readjson.details(set_name)
    myfunc_results = p1.myfunc()
    return myfunc_results



def checks(set_name):
    p1 = readjson.contsets(set_name)
    myfunc_results = p1.myfunc()
    return myfunc_results



#schedule.every(30).seconds.do(checkd)

def val_check():
    try:
    
        #schedule.run_pending()
        
        ph_set =float(checks('PH'))
        ph_var =float(checkd('PH'))
        print(ph_set)
        print(ph_var)
        if ph_set < ph_var:
            relaytest.phdoff()
            print('ph pump on')
            #a = 1
            time.sleep(.6)
            relaytest.phdon()
            #GPIO.cleanup()
        elif ph_set > ph_var:
            print('ph pump off')
            
            

    except SystemExit:
        print('oh snap')
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[1])

    

        
if __name__ == "__main__":
    main()