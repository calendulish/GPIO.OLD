#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

RED = 23
GREEN = 15
BLUE = 27

GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

pwmRED = GPIO.PWM(RED, 120)
pwmGREEN = GPIO.PWM(GREEN, 120)
pwmBLUE = GPIO.PWM(BLUE, 120)

pwmBLUE.start(0)
pwmRED.start(0)
pwmGREEN.start(0)

def degrade(ifcolor, ofcolor, start, finish, timer):
	for dc in range(start, finish):
		ofcolor.ChangeDutyCycle(dc)
		ifcolor.ChangeDutyCycle(100 - dc)
		if dc == 25 or dc == 50 or dc == 75:
			sleep(0.01)
		else:
			sleep(timer)
	sleep(1)
try:
	while True:
		degrade(pwmRED, pwmBLUE, 0, 100, 0.001)
		degrade(pwmBLUE, pwmGREEN, 0, 100, 0.001)
		degrade(pwmGREEN, pwmRED, 0, 100, 0.001)
except KeyboardInterrupt:
	pwmBLUE.stop()
	pwmRED.stop()
	pwmGREEN.stop()
	GPIO.cleanup()
	exit(0)
