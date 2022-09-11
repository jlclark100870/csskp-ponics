import time
import sys
import readjson
import relaytest
# import RPi.GPIO as GPIO
import logging
import poniclog

# ---------------air temp fan control----------------------------


def main():
    relaytest.phdon()
    relaytest.phuon()

    while True:
        checkg('plantdate')
        


def checkd(set_name):
   
    print('checkd')
    print(set_name)
    p1 = readjson.details(set_name)
    myfunc_results = p1.myfunc()
    print(myfunc_results)
    return myfunc_results


def checks(set_name):
    
    print('checks')
    print(set_name)
    p1 = readjson.contsets(set_name)
    myfunc_results = p1.myfunc()
    print(myfunc_results)
    return myfunc_results

def checkg(set_name):
    print('checkg')
    print(set_name)
    p1 = readjson.globalset(set_name)
    myfunc_results = p1.myfunc()
    print(myfunc_results)
    return myfunc_results


def ph_check():
    try:
        ph_dosing = float(checkg('phdosing'))
        ph_set = float(checks('PH'))
        ph_var = float(checkd('PH'))
        print('ph settings')
        print(ph_set)
        print('ph details')
        print(ph_var)

        if ph_set < ph_var:
             relaytest.phdoff()
             print('ph down pump on')
             logging.info('PH down pump on')
             time.sleep(ph_dosing)
             relaytest.phdon()

        elif ph_set > ph_var:
              
              relaytest.phuoff()
              print('ph up pump on')
              logging.info('PH up pump on')
              time.sleep(ph_dosing)
              relaytest.phuon()

        elif ph_set == ph_var:
          
             print('ph pump off')
             logging.info('PH pump off')

    except SystemExit:
            print('oh snap')
    except OSError as err:
            print("OS error: {0}".format(err))
    except ValueError:
            print("Could not convert data to an integer.")
    except:
            print("Unexpected error:", sys.exc_info()[1])

def ec_check():
    try:
    
        ec_dosing = float(checkg('ecdosing'))
        ec_set =float(checks('EC'))
        ec_var =float(checkd('EC'))
        print('ec settings')
        print(ec_set)
        print('ec details')
        print(ec_var)
        if ec_set > ec_var:
            relaytest.ecuoff()
            print('ec pump on')
            time.sleep(ec_dosing)
            relaytest.ecuon()
        elif ec_set <= ec_var:
            print('ec pump off')
            
            

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