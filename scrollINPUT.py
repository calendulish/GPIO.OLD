#!/usr/bin/env python2

import max7219.led as led
import max7219.transitions as transitions
from time import sleep

led.init()

def scroll():
    while True:
        text = raw_input('Escreva algo: ')
        led.show_message(text, transition = transitions.left_scroll)

try:
    scroll()

except KeyboardInterrupt:
    led.letter(0x01)
    print('\nXau!')
    sleep(1)
    led.clear()
    exit(0)
