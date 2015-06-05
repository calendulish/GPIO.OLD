# GPIO Playground ![Raspberry](http://web.craft.net.br/imghp/Diversas/Rasp_turn_around.gif "Raspberry")

[![Join the chat at https://gitter.im/RaspberryLove/GPIO](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/RaspberryLove/GPIO?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

All files in this repository is distributed under the terms of the GNU General Public License
as published by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

For contributors: Please, keep the list in alphabetical order.

## File List

| File            | Description                                               | Language      | Library    |
|-----------------|-----------------------------------------------------------|---------------|------------|
| btnCTRL.py      | Input control with multiple buttons                       | Python 3      | RPi.GPIO   |
| btnGAME         | Simple game using leds and buttons                        | Python 3      | RPi.GPIO   |
| btnRGB.py       | Input control for RGB leds                                | Python 3      | RPi.GPIO   |
| gpioMorse.py    | Translate phrases in morse code for led/buzzer            | Python 3      | RPi.GPIO   |
| LEDMatrix       | Controls multis max7219 LED matrices                      | Python 2      | mlMAX7219  |
| MatrixASCII     | Draw ASCII forms in a 8x8 led matrix                      | C (std c99)   | wiringpi2  |
| MatrixScroll.c  | Draw a scrolling heart in a 8x8 led matrix                | C (std c99)   | wiringpi2  |
| MatrixScroll.py | Draw a scrolling heart in a 8x8 led matrix                | python 3      | RPi.GPIO   |
| MatrixTest.c    | Draw a static heart in a 8x8 led matrix                   | C (std c99)   | wiringpi2  |
| MatrixTest.py   | Draw a static heart in a 8x8 led matrix                   | Python 3      | RPi.GPIO   |
| RGBLed.py       | Transitions with RGB leds (with fade)                     | Python 3      | RPi.GPIO   |
| scrollCLI.py    | Scroll a text in a max7219 controlled led matrix, CLI ver | Python 2      | max7219    |
| scrollINPUT.py  | Scroll a text in a max7219 controlled led matrix          | Python 2      | max7219    |
| spkMusic        | Melody player (Deprecated! Use RPiMusic instead)          | Python 3      | wiringpi2  |
| spkNotes2.py    | Audio test using the library softTone of wiringpi2        | Python 3      | wiringpi2  |
| spkNotes.py     | Audio test using software pwm (very ugly!)                | Python 3      | RPi.GPIO   |
| spkTST-DMA.py   | Frequency loop, using hardware pwm                        | Python 3      | wiringpi2  |
| spkTST.py       | Simple test of audio with frequency loop                  | Python 3      | RPi.GPIO   |

## Libraries
| Library                 | Repository                                                                     |
|-------------------------|--------------------------------------------------------------------------------|
| max7219                 | https://github.com/rm-hull/max7219                                             |
| mlmax7219               | https://github.com/tutRPi/multilineMAX7219                                     |
| RPi.GPIO                | http://sourceforge.net/p/raspberry-gpio-python/code/ci/default/tree/           |
| RPiMusic                | https://github.com/RaspberryLove/RPiMusic                                      |
| wiringpi2 (C and C++)   | https://git.drogon.net/?p=wiringPi                                             |
| wiringpi2 (Python3)     | https://github.com/Gadgetoid/WiringPi2-Python                                  |


NO WARRANTY EXPRESSED OR IMPLIED. IF IT CAUSES A NUCLEAR EXPLOSION I'M NOT RESPONSIBLE.

*Lara Maia <lara@craft.net.br>*

*Fernando Manfredi <blackice@craft.net.br>*
