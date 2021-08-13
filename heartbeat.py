#!/usr/bin/env python
"""
Check to see if an process is running. If not, restart.
Run this in a cron job
"""
import os
import time
import poniclog


process_name= "metamain.py" # change this to the name of your process

tmp = os.popen("ps -Af").read()

while True:
	try:


		if process_name not in tmp[:]:
			poniclog.logging.info ("The process is not running. Let's restart.")
			""""Use nohup to make sure it runs like a daemon"""
			newprocess="nohup python3 %s &" % (process_name)
			os.system(newprocess)  
		else:
			poniclog.logging.info ("The process is running.")

		time.sleep(150)
	except:

            poniclog.logging.exception("Exception in main()")
