#!/usr/bin/python3

import subprocess
import threading
from time import sleep
while True:
        try:
            subprocess.call(["python3", "/home/pi/Desktop/myponic/port.py"])
            print("reset")
        except Exception as e:
            print(e)
        sleep(50)