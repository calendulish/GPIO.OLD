#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from time import sleep, strftime
import LEDMatrix
from fonts import TINY_FONT
from LEDMatrix import DIR_RD

LEDMatrix.init()

def tick():
    while True:
        H = strftime('%H')
        M = strftime('%M')
        S = strftime('%S')
        LEDMatrix.static_message(H+M+S, DIR_RD, 0, TINY_FONT)

def end():
    LEDMatrix.clear_all()
    exit(0)

try:
    tick()

except KeyboardInterrupt:
    end()
