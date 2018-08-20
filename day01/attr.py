# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np

a = np.array([
    [1 + 1j, 2 + 4j, 3 + 7j],
    [4 + 2j, 5 + 5j, 6 + 8j],
    [7 + 3j, 8 + 6j, 9 + 9j],
])
# b = a.shape()

print(a.dtype, a.dtype.str, a.dtype.char)
print(a.shape)
print(a.ndim)
print(a.size, len(a))
print(a.itemsize)
print(a.nbytes)
print(a.T)
print(a.real)
print(a.imag)
for item in a.flat:
    print(item)
