# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# reshape.py
import numpy as np

a = np.arange(1, 9)
# print(a)
b = a.reshape(2, 4)
# print(b)
c = a.reshape(2, 2, 2)
# print(c)
d = c.flatten()
# print(d)
e = c.ravel()
# print(d)
f = c.T
# print(c)
# print(f)
# g = c.swapaxes(a, c)
# print(a, c, sep='\n')

a += 10
# print(a, b, c, d, e, sep='\n')

i = np.arange(11, 20).reshape(3, 3)
j = np.arange(21, 30).reshape(3, 3)
# c = np.vstack((i, j))
# a, k = np.vsplit(c, 2)
# print(c)
# print(a, k)
print(i)
k = np.dstack((i, j))
print(k)
p, q = np.dsplit(k, 2)
print(p.T[0], q, sep='\n')
a, b = p.ravel(), q.ravel()
# c = np.column_stack((a, b))
# c = np.row_stack((a, b))
c = np.vstack((a, b))
print(c)
