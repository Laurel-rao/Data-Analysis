# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# dtype.py

import numpy as np

a = np.array([20, 22, 28, 25, 19])
print(a.dtype)

b = np.array([20, 22, 28, 25, 19], dtype=np.uint8)
print(b.dtype)
c = np.array([('ABC', (1, 2, 3))], dtype='U3, 3u1')
print(c.dtype)
e = np.array([('ABC', (1, 2, 3))], dtype={'names': ['fa', 'fb'], 'formats':
                                          ['U3', '3u1']})
d = np.array([('ABC', (1, 2, 3))], dtype=[
             ('fa', np.str_, 3),
             ('fb', np.uint8, 3)])

f = np.array([('ABC', (1, 2, 3))], dtype={'fa': ('U3', 0), 'fb': ('3u1', 12)})

print(f[0]['fa'], f[0]['fb'])
