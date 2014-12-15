#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from time import sleep, strftime
import LEDMatrix
from fonts import TINY_FONT
from LEDMatrix import DIR_RD, DIR_L

LEDMatrix.init()

def tick():
    while True:
        date = strftime('%a') + " " + strftime('%x')
        LEDMatrix.scroll_message_horiz([date], 1, 5, DIR_L, TINY_FONT)
        sleep(1)
        cycle = 1
        while cycle < 80:
            H = strftime('%H')
            M = strftime('%M')
            S = strftime('%S')
            LEDMatrix.static_message(H+M+S, DIR_RD, 0, TINY_FONT)
            cycle += 1
            sleep(0.5)

def end():
    LEDMatrix.clear_all()
    exit(0)

try:
    tick()

except KeyboardInterrupt:
    end()
