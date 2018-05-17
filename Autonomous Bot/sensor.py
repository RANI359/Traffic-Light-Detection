import RPi.GPIO as gpio
import time

def distance(measure='cm'):
	gpio.setmode(gpio.BOARD)
	gpio.setup(33, gpio.OUT)
	gpio.setup(35, gpio.IN)
	
	gpio.output(33, False)
	while gpio.input(35) == 0:
		nosig = time.time()
	
	while gpio.input(35) == 1:
		sig = time.time()
		
	t1 = sig - nosig
	
	if measure == 'cm':
		distance = t1/0.000058
	elif measure == 'in':
		distance = t1/0.000148
	else:
		print('improper choice of measurement: in or cm')
		distance = None
		
	gpio.cleanup()
	return distance
	
print(distance('cm'))
		
