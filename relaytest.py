import RPi.GPIO as GPIO
import time

in1 = 16
in2 = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)

def phdon():
    GPIO.output(in1, True)

def phdoff():
    GPIO.output(in1, False)
    
def lighton():
    GPIO.output(in2, True)

def lightoff():
    GPIO.output(in2, False)
   
