#!/usr/bin/python3

import subprocess
import threading
from time import sleep
import logging
from datetime import datetime

now = str(datetime.now())

while True:
        try:
            subprocess.call(["python3", "/home/pi/Desktop/myponic/port.py"])
            print("reset")
        except Exception as e:
            print(e)
            logging.info(now)
            logging.info('RESET')
            logging.info('--------------------------------------------------------------------------------------------------------')
        sleep(50)