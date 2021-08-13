import serial
import time
from datetime import datetime
import sys


#set up serial and open text file

dataFile = open('dataFile.txt', 'w')
ser = serial.Serial('COM3', 9600, timeout=1)




        
while True:
    data = ser.readline()
    if data:
        dataFile.write(data)
        dataFile.write("\r")
        print (data)         
           
