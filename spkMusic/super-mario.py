#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    Copyright (C) 2014 Lara Maia <lara@craft.net.br>
#
#    This file is part of spkMusic.
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
#

delay = 50

melody = [
          'E6:',
          'E6',  '',
          'E6',  '',
          'C6',
          'E6',  '',
          'G6',  '',
          'G5',  '',

          'C6',  '',
          'G5',  '',
          'E5',  '',
          'A5:',
          'B5:',
          'Bb5:',
          'A5:',

          'G5',
          'E6',
          'G6',
          'A6',  '',
          'F6',
          'G6',  '',
          'D6',  '',
          'C6',
          'D6',
          'B5',

          'C6',  '',
          'G5',  '',
          'E5',  '',
          'A5:',
          'B5:',
          'Bb5:',
          'A5:',

          'G5',
          'E6',
          'G6',
          'A6',  '',
          'F6',
          'G6',  '',
          'D6',  '',
          'C6',
          'D6',
          'B5',  '',

          # PARTE 2

          'G6:',
          'G6',
          'F6',
          'D#6', '',
          'E6',  '',
          'G#5',
          'A5',
          'C6',  '',
          'F5',
          'C6',
          'D6',  '',

          'G6',
          'Gb6',
          'F6',
          'D#6', '',
          'E6',  '',
          'C7',  '',
          'C7',
          'C7',
          'G5', '',

          'C5', '',
          'G6:',
          'G6',
          'F6',
          'D#6', '',
          'E6',  '',
          'G#5',
          'A5',
          'C6',  '',
          'F5',
          'C6',
          'D6',  '',

          'C5',  '',
          'Eb6', '',
          'D6',  '',
          'C6',  '',
          'G5:',
          'G5',  '',
          'C5',  '',

           # PARTE 3

          'G6:',
          'G6',
          'F6',
          'D#6', '',
          'E6',  '',
          'G#5',
          'A5',
          'C6',  '',
          'F5',
          'C6',
          'D6',  '',

          'G6',
          'Gb6',
          'F6',
          'D#6', '',
          'E6',  '',
          'C7',  '',
          'C7',
          'C7',
          'G5', '',

          'C5', '',
          'G6:',
          'G6',
          'F6',
          'D#6', '',
          'E6',  '',
          'G#5',
          'A5',
          'C6',  '',
          'F5',
          'C6',
          'D6',  '',

          'C5',  '',
          'Eb6', '',
          'D6',  '',
          'C6',  '',
          'G5:',
          'G5',  '',
          'C5',  '',
          ]

beats = [
          1,
          1, 2,
          1, 2,
          1,
          1, 2,
          1, 6,
          1, 6,

          1, 6,
          1, 6,
          1, 6,
          2,
          2,
          1,
          2,

          2,
          2,
          2,
          2, 1,
          1,
          1, 1,
          1, 1,
          2,
          2,
          2,

          1, 6,
          1, 6,
          1, 6,
          2,
          2,
          1,
          2,

          2,
          2,
          2,
          2, 1,
          1,
          1, 1,
          1, 1,
          2,
          3,
          1, 6,

          # PARTE 2

          2,
          2,
          2,
          1, 2,
          1, 2,
          2,
          2,
          1, 2,
          2,
          2,
          1, 2,

          2,
          2,
          2,
          1, 2,
          1, 2,
          1, 1,
          1,
          1,
          2,
          1, 6,

          1, 6,
          2,
          2,
          2,
          1, 2,
          1, 2,
          2,
          2,
          1, 2,
          2,
          2,
          1, 2,

          1, 2,
          1, 2,
          2, 2,
          2, 2,
          1,
          2, 6,
          1, 10,

          # PARTE 3

          2,
          2,
          2,
          1, 2,
          1, 2,
          2,
          2,
          1, 2,
          2,
          2,
          1, 2,

          2,
          2,
          2,
          1, 2,
          1, 2,
          1, 1,
          1,
          1,
          3,
          1, 6,

          1, 6,
          2,
          2,
          2,
          1, 2,
          1, 2,
          2,
          2,
          1, 2,
          2,
          2,
          1, 2,

          1, 2,
          1, 2,
          2, 2,
          2, 2,
          1,
          2, 6,
          1, 10,
        ]


