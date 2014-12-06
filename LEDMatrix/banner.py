#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from sys import argv
from time import sleep

import LEDMatrix
from fonts import CP437_FONT, SINCLAIRS_FONT, LCD_FONT, TINY_FONT
from LEDMatrix import DIR_L, DIR_R

LEDMatrix.init()

def scroll(text, cycles=1, speed=5):
    speed=float(speed)
    LEDMatrix.scroll_message_horiz([text + "  "], cycles, speed, DIR_L, TINY_FONT)

def end():
    sleep(1)
    LEDMatrix.clear_all()
    exit(0)

def usage():
    print('\nTry: \n banner.py "your text" [cycles] [speed]')

try:
    argv.pop(0)
    scroll(*argv)
    end()

except TypeError:
    usage()
except KeyboardInterrupt:
    end()
