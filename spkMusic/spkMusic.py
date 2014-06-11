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
import importlib
import curses
import sys

class Play:
    def __init__(self):

        wiringpi2.wiringPiSetupGpio()

        self.SPEAKER = 18
        self.MODE_PWM = 2

        self.divisor = (19.2*(10**3))/440

        wiringpi2.pinMode(self.SPEAKER, self.MODE_PWM)
        wiringpi2.pwmSetMode(wiringpi2.GPIO.PWM_MODE_MS)

        screen = curses.initscr()
        curses.start_color()
        self.window = curses.newwin(10, 80, 5, 5)

        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

    def calcParams(self, note):
        labels = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

        noteName = note

        # Precisamos calcular a frequências das notas de forma
        # transparente. Acompanhe a seguinte explicação:
        # http://www.bigcomposer.com/module/lectures/notation2.pdf
        # Tendo um sistema musical que divide oitavas em 12 intervalos
        # iguais de meio-passos (como em um piano), temos que:
        # freq = nota mais baixa possível x ((2^(1/12))^((oitava*12)+nota))
        if len(note) == 3:
            if note[1:2] == 'b':
                note = labels[ labels.index( note[0:1] ) -1 ]+note[2:3]

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

        self.window.box()
        self.window.addstr(1, 25, 'spkMusic - Lara Maia <lara@craft.net.br>', curses.color_pair(1))
        self.window.addstr(3, 25, 'note: {:3}'.format(noteName), curses.color_pair(2))
        self.window.addstr(4, 25, 'freq: {:.3f}'.format(freq), curses.color_pair(2))
        self.window.addstr(5, 25, 'period: {:.3f}'.format(period), curses.color_pair(2))
        self.window.addstr(6, 25, 'dutyCycle: {:.3f}'.format(dutyCycle), curses.color_pair(2))
        self.window.refresh()

        return (int(period), int(dutyCycle))

    def main(self):
        wiringpi2.pwmSetClock(int(self.divisor))

        for i, note in enumerate(Music.melody):
            if len(note) == 0:
                wiringpi2.pwmWrite(self.SPEAKER, 0)
                wiringpi2.delay(62*(Music.beats[i]+1))
            else:
                period, dutyCycle = self.calcParams(note)
                wiringpi2.pwmSetRange(period)
                wiringpi2.pwmWrite(self.SPEAKER, dutyCycle)

                wiringpi2.delay(125*(Music.beats[i]+1))

        curses.endwin()
        wiringpi2.pinMode(self.SPEAKER, 0)

if __name__ == "__main__":
    try:
        Music = importlib.import_module(sys.argv[1])
        play = Play()
        play.main()
    except IndexError:
        print("Cade a música? '-'")
        exit(1)
    except ImportError as ex:
        print("Não dá pra encontrar nada nessa bagunça '-'")
        print(ex)
        exit(1)
