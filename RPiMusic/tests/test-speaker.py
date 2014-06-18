#!/usr/bin/env python

import sys
sys.path.append('..')

import RPiMusic

pMusic = RPiMusic.Melody()

try:
    pMusic.spkPlay('do-re-mi-fa')
    pMusic.end()
except ImportError as e:
    print('Melody {} not found'.format(str(e)[17:-1]))
