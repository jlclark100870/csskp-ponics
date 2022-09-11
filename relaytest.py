#import RPi.GPIO as GPIO
import time
import logging
# GPIO.setwarnings(False)


# in1 = 32
# in2 = 12
# in3 = 18
# in4 = 16
# in5 = 8


# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(in1, GPIO.OUT)
# GPIO.setup(in2, GPIO.OUT)
# GPIO.setup(in3, GPIO.OUT)
# GPIO.setup(in4, GPIO.OUT)
# GPIO.setup(in5, GPIO.OUT)

def main():
    ecuon()
    phdon()
    phuon()
    lighton()  
    tempoff()  
    time.sleep(2)
    lightoff()

   
 
 




def phdon():
    #GPIO.output(in1, True)
    print('ph down on')
    logging.info('ph down on')

def phdoff():
    #GPIO.output(in1, False)
    print('ph down off')
    logging.info('ph down off')
    
def lighton():
    #GPIO.output(in2, True)
    print('light on')
    logging.info('light on')

def lightoff():
    #GPIO.output(in2, False)
    print('light off')
    logging.info('light off')

def phuon():
    #GPIO.output(in3, True)
    print('ph up on')
    logging.info('ph up on')

def phuoff():
    #GPIO.output(in3, False)
    print('ph up off')
    logging.info('ph up off')

def tempon():
    #GPIO.output(in4, False)
    print('temp on')
    logging.info('temp on')

def tempoff():
    #GPIO.output(in4, True)
    print('temp off')
    logging.info('temp off')

def ecuon():
    #GPIO.output(in5, True)
    print('ec on')
    logging.info('ec on')

def ecuoff():
    #GPIO.output(in5, False)
    print('ec off')
    logging.info('ec off')

def humidon():
    print('humidifier on')
    logging.info('humidifier on')

def humidoff():
    print('humidifier off')
    logging.info('humidifier off')







if __name__ == "__main__":
    main()