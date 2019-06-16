#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time, sys

GPIO.setmode(GPIO.BCM)


GPIO.setup(17, GPIO.IN)
if GPIO.input(17) == True:
    print("probably on")

sys.exit()
#init list with pin
PinList = [17]

for p in PinList:
    GPIO.setup(p, GPIO.OUT)
    GPIO.output(p, GPIO.HIGH)

#pin_is_on = GPIO.input(PinList[0])
#print(pin_is_on)

try:
	for p in PinList:
		print("Light off")
		#High turns the pins off.
		GPIO.output(p, GPIO.HIGH)	
	GPIO.cleanup()
except KeyboardInterrupt:
	print("\n\tCommand from Keyboard  to Quit")
	GPIO.cleanup()
except Exception as e:
	print("An error has occured\n\t{}".format(e))
	GPIO.cleanup()
