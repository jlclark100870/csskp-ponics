#!/usr/bin/python

import time # Time access and conversions
from binascii import hexlify
from array import array
import smbus


import io
import sys
import fcntl
import time
import copy
import string


def phread():
	from AtlasI2C import AtlasI2C
	sensor_address = 99
	dev = AtlasI2C()
	dev.set_i2c_address(sensor_address)
	dev.write("R")
	time.sleep(1.5)
	result = dev.read(4)
	return(result)

def ecread():
	from AtlasI2C import AtlasI2C
	sensor_address = 100
	dev = AtlasI2C()
	dev.set_i2c_address(sensor_address)
	dev.write("R")
	time.sleep(1.5)
	usresult = dev.read(4)
	try:
		result = float(usresult)/100
		print(result)
	except:
		result = 0.00
		print("oops")
	return(result)
"""
while True:
	print(ecread())
"""
