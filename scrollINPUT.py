#!/usr/bin/env python2

import max7219.led as led
import max7219.transitions as transitions

led.init()

def scroll():
    while True:
        text = raw_input('Escreva algo: ')
        led.show_message(text, transition = transitions.left_scroll)

try:
    scroll()

except KeyboardInterrupt:
    led.show_message("Xau", transition = transitions.up_scroll)
    led.clear()
    print('\nXau!')
    exit(0)
