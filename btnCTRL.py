#!/usr/bin/env python
# Versaum 0.1

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

BLUE = 25
GREEN = 24
RED = 23
BTN1 = 4
BTN2 = 22
BTN3 = 17

GPIO.setup(BLUE, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(GREEN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(RED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(BTN1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BTN2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BTN3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

COR = 1

def BTN_dir(BTN1):
    global COR
    COR += 1
    print("Botaum direito pressionado")

def BTN_esq(BTN2):
    global COR
    COR -= 1
    print("Botaum esquerdo pressionado")

def led():
    global COR
    while True:
        if COR == 0:
            GPIO.output(BLUE, True)
            GPIO.output(GREEN, False)
            GPIO.output(RED, False)
        elif COR == 1:
            GPIO.output(BLUE, False)
            GPIO.output(GREEN, True)
            GPIO.output(RED, False)
        elif COR == 2:
            GPIO.output(BLUE, False)
            GPIO.output(GREEN, False)
            GPIO.output(RED, True)
        elif COR > 2:
            COR = 0
        elif COR < 0:
            COR = 2

def sair(status):
    print("TCHAU... :(")
    GPIO.cleanup()
    exit(status)

GPIO.add_event_detect(BTN1, GPIO.BOTH)
GPIO.add_event_callback(BTN1, callback=BTN_dir, bouncetime=300)

GPIO.add_event_detect(BTN2, GPIO.BOTH)
GPIO.add_event_callback(BTN2, callback=BTN_esq, bouncetime=300)

GPIO.add_event_detect(BTN3, GPIO.BOTH)
GPIO.add_event_callback(BTN3, callback=sair, bouncetime=300)

try:
    led()
except KeyboardInterrupt:
    sair(0)
sair(0)
