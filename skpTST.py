#!/usr/bin/env python
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

SPEAKER = 17
GPIO.setup(SPEAKER,GPIO.OUT)

try:
    while True:
        GPIO.output(SPEAKER,True)
        sleep(0.25)
        GPIO.output(SPEAKER,False)
except KeyboardInterrupt:
    GPIO.cleanup()
exit()
