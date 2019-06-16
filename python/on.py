#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#init list with pin

PinList = [17]
for p in PinList:
    GPIO.setup(p, GPIO.OUT)
    GPIO.output(p, GPIO.HIGH)
	
try:
    for p in PinList:
        GPIO.output(p, GPIO.LOW)
		#print("Pin {} is on.".format(p))
        print("Light is on.")
    
except KeyboardInterrupt:
	print("\n\tCommand from Keyboard  to Quit")
	GPIO.cleanup()
except Exception as e:
	print("An error has occured\n\t{}".format(e))
	
	GPIO.cleanup()
