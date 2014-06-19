#!/usr/bin/env python

import wiringpi2
from time import sleep

wiringpi2.wiringPiSetupGpio()

SPEAKER = 18

# Escala da 5° oitava
C = 523
D = 587
E = 659
F = 698
G = 783
A = 880
B = 987

C6 = 1046

wiringpi2.softToneCreate(SPEAKER)

for freq in [ C, D, E, F, G, A, B, C6 ]:
    wiringpi2.softToneWrite(SPEAKER, freq)
    sleep(0.5)

wiringpi2.digitalWrite(SPEAKER, 0)
wiringpi2.pinMode(SPEAKER, 0)
exit(0)
