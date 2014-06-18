#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    Copyright (C) 2014 Lara Maia <lara@craft.net.br>
#
#    spkMusic is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    http://www.gnu.org/licenses/gpl.html
#

import wiringpi2
from importlib import import_module

class Melody:
    def __init__(self):
        wiringpi2.wiringPiSetupGpio()

        self.SPEAKER = 18
        self.MODE_PWM = 2

        wiringpi2.pinMode(self.SPEAKER, self.MODE_PWM)
        wiringpi2.pwmSetMode(wiringpi2.GPIO.PWM_MODE_MS)

        wiringpi2.pwmWrite(self.SPEAKER, 0)

    def _calcParams(self, note):
        labels = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

        if len(note) >= 3 and not note[2:3] == ':' and not note[2:3] == ';':
            if note[1:2] == 'b':
                note = labels[labels.index(note[0:1])-1]+note[2:3]

            octave = int(note[2:3])*12
            note = labels.index(note[0:2])
        else:
            octave = int(note[1:2])*12
            note = labels.index(note[0:1])

        freqBase = 16.351 # C0
        magicNumber = 2**(1/12)

        freq = freqBase*(magicNumber**(octave+note))

        period = (1/freq)*(10**6)
        dutyCycle = period/2

        return (int(period), int(dutyCycle))

    def _playLoop(self, freq, music):
        divisor = (19.2*(10**3))/freq
        Music = import_module(music)

        wiringpi2.pwmSetClock(int(divisor))

        for note, beat in Music.melody:
            if note == ' ':
                wiringpi2.pwmWrite(self.SPEAKER, 0)
            else:
                period, dutyCycle = self._calcParams(note)
                wiringpi2.pwmSetRange(period)
                wiringpi2.pwmWrite(self.SPEAKER, dutyCycle)

            wiringpi2.delay(Music.tempo*beat)

            if note[len(note)-1:] == ':':
                wiringpi2.pwmWrite(self.SPEAKER, 0)
                wiringpi2.delay(Music.tempo)
            elif note[len(note)-1:] == ';':
                wiringpi2.pwmWrite(self.SPEAKER, 0)
                wiringpi2.delay(int(Music.tempo/2))

        # Make sure that music stop
        wiringpi2.pwmWrite(self.SPEAKER, 0)

    def buzzerPlay(self, music):
        self._playLoop(2400, music)

    def spkPlay(self, music):
        self._playLoop(440, music)

    def ledPlay(self, music):
        pass # STUB

    def end(self):
        wiringpi2.pinMode(self.SPEAKER, 0)
        wiringpi2.pwmSetMode(wiringpi2.GPIO.PWM_MODE_BAL)
