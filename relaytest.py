import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)


in1 = 32
in2 = 12
in3 = 18
in4 = 16
in5 = 8


GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(in5, GPIO.OUT)

def main():
    ecuon()
    phdon()
    phuon()
    lighton()  
    tempoff()  
    time.sleep(2)
    lightoff()

   
 
 




def phdon():
    GPIO.output(in1, True)

def phdoff():
    GPIO.output(in1, False)
    
def lighton():
    GPIO.output(in2, True)

def lightoff():
    GPIO.output(in2, False)

def phuon():
    GPIO.output(in3, True)

def phuoff():
    GPIO.output(in3, False)

def tempon():
    GPIO.output(in4, False)

def tempoff():
    GPIO.output(in4, True)

def ecuon():
    GPIO.output(in5, True)

def ecuoff():
    GPIO.output(in5, False)







if __name__ == "__main__":
    main()