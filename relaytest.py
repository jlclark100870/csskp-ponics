import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)


in1 = 12
in2 = 18
in3 = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)



def main():
    ecuon()
    phdon()
    lighton()
    time.sleep(2)
    lightoff()
    time.sleep(2)





def phdon():
    GPIO.output(in1, True)

def phdoff():
    GPIO.output(in1, False)
    
def lighton():
    GPIO.output(in2, True)

def lightoff():
    GPIO.output(in2, False)

def ecuon():
    GPIO.output(in3, True)

def ecuoff():
    GPIO.output(in3, False)




if __name__ == "__main__":
    main()