#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import max7219.led as led
import max7219.transitions as transitions
import sys
from time import sleep

led.init()

def scroll(text, cycles):
    i = 0
    while i < cycles:
        led.show_message(text, transition = transitions.left_scroll)
        i += 1

def end():
    led.letter(0x01)
    print('\nXau!')
    sleep(1)
    led.clear()
    exit(0)

def usage():
    print('\nTry: \n scrollCLI.py "your text" X\nWhere "X" is a number of transitions.')

try:
    scroll(sys.argv[1], int(sys.argv[2]))
    end()

except IndexError:
    usage()
except KeyboardInterrupt:
    end()
