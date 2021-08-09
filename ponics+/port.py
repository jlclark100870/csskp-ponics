import requests
import serial
from time import sleep, time
import json
import serial.tools.list_ports
ports = list(serial.tools.list_ports.comports())
for p in ports:
    print(p)
    ser = serial.Serial(p.device, 9600, timeout=0)
url = 'http://csskp.com/api/v1/machine/test.php'
def read():
    
    ser.reset_input_buffer()
    seq=[]
    timeout = time() + 5   # 5 minutes from now
    while time() < timeout:
        try:
            for c in ser.read():
                seq.append(chr(c)) #convert from ANSII
                if chr(c) == '#':
                    joined_seq = ''.join(str(v) for v in seq) #Make a string from array
                    rawData = joined_seq[1:-1].split(',')
                    data = {
                        'humidity' : float(rawData[0]),
                        'air_temp' : float(rawData[1]),
                        'lightSensor' : int(rawData[2]),
                        'water_temp' : float(rawData[3])
                        }
                    #print(data)
                    #with open("data.txt", "w") as write_file:
                        #json.dump(data, write_file, indent=4)

                    myobj = json.dumps(data)

                    x = requests.post(url, myobj)

                    #print the response text (the content of the requested file):
                    print(data)
                    
                    
        except:
            seq=[]
            print("Waiting for data")
            sleep(1)
            
            
while True:
    read()
   
