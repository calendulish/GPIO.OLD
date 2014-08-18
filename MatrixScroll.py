#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

# --------- > p0, p1, p2, p3, p4, p5, p6, p7
pins1 = [ -1, 17, 18, 27, 22, 23, 24, 25, 4 ]

# --------- > ce1, ce0, sclk, miso, mosi, rxd, txd, scl
pins2 = [ -1,  7,   8,   11,   9,    10,   15,  14,  3 ]

# --------- >   p0    17  p5    24  scl   3   p3    22  ce1   7   txd   14  ce0   8   mosi  10
rows    = [ -1, pins1[1], pins1[6], pins2[8], pins1[4], pins2[1], pins2[7], pins2[2], pins2[5] ]

# --------- >   p4    23  sclk  11  miso  9   p1    18  rxd   15  p2    27  p6    25  p7    4
columns = [ -1, pins1[5], pins2[3], pins2[4], pins1[2], pins2[6], pins1[3], pins1[7], pins1[8] ]


for i in range(1, 9):
    GPIO.setup(rows[i], GPIO.OUT)
    GPIO.setup(columns[i], GPIO.OUT)
    GPIO.output(rows[i], GPIO.LOW)
    GPIO.output(columns[i], GPIO.LOW)

def _exit(status):
    GPIO.cleanup()
    exit(status)

def led(column, row, status):
    for col in range(1, 9):
        if col != column:
            GPIO.output(columns[col], status)
    GPIO.output(rows[row], status)

def draw(column, row, delay=0.001):
    led(column, row, GPIO.HIGH)
    sleep(delay)
    led(column, row, GPIO.LOW)

try:
    while True:
        for i in range(0, 24):
            i=8-i
            draw(3+i, 1)
            draw(2+i, 2)
            draw(1+i, 3)
            draw(1+i, 4)
            draw(2+i, 5)
            draw(3+i, 6)
            draw(4+i, 7)
            draw(5+i, 6)
            draw(6+i, 5)
            draw(7+i, 4)
            draw(7+i, 3)
            draw(6+i, 2)
            draw(5+i, 1)
            draw(4+i, 2)
            sleep(0.04)
except KeyboardInterrupt:
	_exit(0)
_exit(0)
