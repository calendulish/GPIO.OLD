#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import max7219.led as led
import max7219.transitions as transitions
import sys
from time import sleep

led.init()

def scroll():
    i = 0
    text = sys.argv[1]
    cycles = int(sys.argv[2])
    while(i < cycles):
        led.show_message(text, transition = transitions.left_scroll)
        i += 1
    end()

def end():
    led.letter(0x03)
    print('\nXau!')
    sleep(1)
    led.clear()
    exit(0)

try:
    scroll()

except KeyboardInterrupt:
    end()
