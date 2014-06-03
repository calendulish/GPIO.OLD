#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

BLUE = 25
GREEN = 24
RED = 23
BTN = 4

GPIO.setup(BLUE, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(GREEN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(RED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(BTN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

POWER = False

def checkBTN(event):
#    print("Fez clic clac (Oia aqui: {}) no pininho: {}".format(GPIO.input(BTN), event))
    global POWER
    if POWER:
        print("DESLIGUEI... Ahhh =(")
        POWER = False
    else:
        print("LIGUEI!!! Uhhuul \o/")
        POWER = True

def pisca():
    while True:
        for led in [ BLUE, GREEN, RED ]:
            if POWER:
                GPIO.output(led, True)
                sleep(0.15)
                GPIO.output(led,False)
            else:
                break

GPIO.add_event_detect(BTN, GPIO.FALLING, callback=checkBTN, bouncetime=500)

try:
    pisca()
except KeyboardInterrupt:
    GPIO.cleanup()
    exit(0)
