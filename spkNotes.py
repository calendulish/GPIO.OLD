#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

SPEAKER = 18
GPIO.setup(SPEAKER, GPIO.OUT)

pwmSPEAKER = GPIO.PWM(SPEAKER, 440)
pwmSPEAKER.start(50)

# Escala da 5° oitava
C = 523.25
D = 587.33
E = 659.25
F = 698.46
G = 783.99
A = 880.00
B = 987.77

C6 = 1046.50

for freq in [ C, D, E, F, G, A, B, C6 ]:
    pwmSPEAKER.ChangeFrequency(freq)
    sleep(0.5)

pwmSPEAKER.stop()
GPIO.cleanup()
exit(0)
