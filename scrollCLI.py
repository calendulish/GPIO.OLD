#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import max7219.led as led
import max7219.transitions as transitions
import sys
from time import sleep

led.init()

def scroll(text, cycles, direction=left):
    i = 0
    while i < int(cycles):
        if(direction == 'up'):
            led.show_message(text, transition = transitions.up_scroll)
        elif(direction == 'simple'):
            led.show_message(text, transition = transitions.simple)
        else:
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
    # If are not available separately, write the function call with
    # the * operator to unpack the arguments out of a list or tuple:
    # https://docs.python.org/2/tutorial/controlflow.html#unpacking-argument-lists
    scroll(*sys.argv)
    end()

except IndexError:
    usage()
except KeyboardInterrupt:
    end()
