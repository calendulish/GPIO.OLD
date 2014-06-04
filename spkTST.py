#!/usr/bin/env python
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

SPEAKER = 17

GPIO.setup(SPEAKER,GPIO.OUT)

pwmSPEAKER = GPIO.PWM(SPEAKER, 1)
pwmSPEAKER.start(5)

try:
    while True:
        for freq in range(500,1000, 1):
            pwmSPEAKER.ChangeFrequency(freq)
            sleep(0.001)
        for freq in range(1000, 500, -1):
            pwmSPEAKER.ChangeFrequency(freq)
            sleep(0.001)
except KeyboardInterrupt:
    pwmSPEAKER.stop()
    GPIO.cleanup()
exit()
