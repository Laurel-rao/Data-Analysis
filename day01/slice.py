# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# slice.py

import numpy as np

a = np.arange(1, 10)
print(a[:3])
print(a[3:6:2])
print(a[::-1])
print(a[:-4:-1])
print(a[-4:-7:-1])
print(a[:])

b = np.arange(1, 25).reshape(2, 3, 4)

print(b)
