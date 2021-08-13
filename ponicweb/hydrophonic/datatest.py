import serial
import time
import csv

ser = serial.Serial('COM3', 9600, timeout=1)
ser.flushInput()

while True:
    
    ser_bytes = ser.readline()
    if (ser_bytes !=""):
       decoded_bytes = ser_bytes[0:len(ser_bytes)-2].decode("utf-8")
       print(decoded_bytes)
       with open("test_data.csv","a") as f:
           writer = csv.writer(f,delimiter=",")
           writer.writerow([decoded_bytes])
    
