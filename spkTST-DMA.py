#!/usr/bin/env python
# Copyright (C) 2014 Lara Maia <lara@craft.net.br>
#
#    This program is free software: you can redistribute it and/or modify
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
from time import sleep

wiringpi2.wiringPiSetupGpio()

# O PWM via hardware funciona somente na GPIO 18
# (Existe outra posibilidade usando o pino 12 do P1)
SPEAKER = 18
MODE_PWM = 2

wiringpi2.pinMode(SPEAKER, MODE_PWM)
wiringpi2.pwmSetMode(wiringpi2.GPIO.PWM_MODE_MS)

# Os tons/notas são criados ao pulsar ao alto-falante usando PWM
# para criar frequências. Cada nota tem uma frequência criada pela
# variação do período de vibração (period of vibration), medido em µs.
# Temos que calcular a largura do pulso (pulse-width) para ser metade
# do período. Basicamente temos que pulsar o alto-falante em HIGH até
# a largura do pulso (pulse-width) e então LOW, da mesma forma. Esses
# pulsos vão criar uma vibração equivalente a frequência desejada.

# Então temos, na ordem:

# 1) Frequência
# freq = A3 = Lá na 3ª oitava
# freq = 440hz

# 2) período
# period = 1s/freq (em hz)
# period = 1/440
# period = 0.002272728s
# Nota: Temos o period em S, mas precisamos em µs
# period = period*1000000 (de s para µs)
# period = 0.002272728*1000000
# period = 2272.728

# 3) Ciclo de trabalho
# dutyCycle = period(µs) / 2p
# dutyCycle = 2272.728 / 2
# dutyCycle = 1136.364

# 4) Divisor do clock
# divisor = clock (hz)/(freq (hz) x period (µs))
# Tendo que o clock base do pwm é 19.2mhz:
# divisor = (19.2x1000000)/(440 x 2272.728)
# divisor = 19200000/1000000.32
# divisor = 19.1999939

def calcParams(freq):
   period = (1/freq)*(10**6)
   divisor = (19.2*(10**6))/(freq*period)
   dutyCycle = period/2
   return (int(period), int(divisor), int(dutyCycle))

try:
    while True:
        for freq in range(500, 1001, 1):
            period, divisor, dutyCycle = calcParams(freq)
            wiringpi2.pwmSetRange(period)
            wiringpi2.pwmSetClock(divisor)
            wiringpi2.pwmWrite(SPEAKER, dutyCycle)
            sleep(0.001)
        for freq in range(1000, 499, -1):
            period, divisor, dutyCycle = calcParams(freq)
            wiringpi2.pwmSetRange(period)
            wiringpi2.pwmSetClock(divisor)
            wiringpi2.pwmWrite(SPEAKER, dutyCycle)
            sleep(0.001)
except KeyboardInterrupt:
    wiringpi2.pwmWrite(SPEAKER, 0)
    wiringpi2.pinMode(SPEAKER, 0)
    exit(0)
