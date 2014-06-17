#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import RPi.GPIO as GPIO
from time import sleep


CODE = {' ': ' ',
        "'": '.----.',
        '(': '-.--.-',
        ')': '-.--.-',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ':': '---...',
        ';': '-.-.-.',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-'
        }

GREEN=24
SPK=18
GPIO.setmode(GPIO.BCM)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(SPK, GPIO.OUT)


def dot():
    GPIO.output(GREEN, 1)
    GPIO.output(SPK, 1)
    sleep(0.1)
    GPIO.output(GREEN, 0)
    GPIO.output(SPK, 0)
    sleep(0.1)


def dash():
    GPIO.output(GREEN, 1)
    GPIO.output(SPK, 1)
    sleep(0.3)
    GPIO.output(GREEN, 0)
    GPIO.output(SPK, 0)
    sleep(0.1)


def morse():
    while True:
        frase = input('O que será enviado? ')
        sleep(0.5)
        for letter in frase:
            for symbol in CODE[letter.upper()]:
                if symbol == '-':
                    dash()
                elif symbol == '.':
                    dot()
                else:
                    sleep(0.5)
                sleep(0.1)
try:
    morse()

except KeyboardInterrupt:
    GPIO.cleanup()
    print('Fui...')
    exit(0)
