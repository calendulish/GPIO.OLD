#!/usr/bin/env python

import RPiMusic

pMusic = RPiMusic.Melody()

try:
    pMusic.buzzerPlay('do-re-mi-fa')
    pMusic.end()
except ImportError as e:
    print('Melody {} not found'.format(str(e)[17:-1]))
