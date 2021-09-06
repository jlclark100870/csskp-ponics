import time
import sys
import readjson
import relaytest
import RPi.GPIO as GPIO
import logging
import poniclog

#---------------air temp fan control----------------------------

def main():
    while True:
        ph_check()
        ec_check()
        time.sleep(50)

def checkd(set_name):
    print('checkd')
    p1 = readjson.details(set_name)
    myfunc_results = p1.myfunc()
    return myfunc_results



def checks(set_name):
    print('checks')
    p1 = readjson.contsets(set_name)
    myfunc_results = p1.myfunc()
    return myfunc_results





def ph_check():
    try:
    
                
        ph_set =float(checks('PH'))
        ph_var =float(checkd('PH'))
        print(ph_set)
        print(ph_var)


        if ph_set < ph_var:
            relaytest.phdoff()
            print('ph down pump on')
            logging.info('PH pump on')
            time.sleep(float(checks('phdosing')))
            relaytest.phdon()


        elif ph_var < 6:
            relaytest.ecuoff()
            print('ph up pump on')
            logging.info('PH up pump on')
            time.sleep(6)
            relaytest.ecuon()


        elif ph_set > ph_var:
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
    
        
        ec_set =float(checks('EC'))
        ec_var =float(checkd('EC'))
        print(ec_set)
        print(ec_var)
        if ec_set > ec_var:
            relaytest.ecuoff()
            print('ec pump on')
            #time.sleep(float(checks('ecdosing')))
            relaytest.ecuon()
        elif ec_set < ec_var:
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