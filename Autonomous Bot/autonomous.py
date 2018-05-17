import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk
from sensor import distance
import random
from test1 import traffic
from autopilot import obstacle

gpio.setmode(gpio.BOARD)
gpio.setup(7, gpio.OUT)
gpio.setup(11, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)

while True:
	a = traffic()
	if a > 1800 and a < 7500:
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(13, False)
		gpio.output(15, False)
		#time.sleep(tf)
	else:
		obstacle()

		
		
gpio.cleanup()
		

		


