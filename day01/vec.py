# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime as dt
import numpy as np

n = 100000

A, B = [], []
C = []


def origin():
    for i in range(n):

        A.append(i**2)
        B.append(i**3)

    for a, b in zip(A, B):
        C.append(a + b)


def nums():
    A, B = np.arange(n)**2, np.arange(n) ** 3
    C = A + B


if __name__ == '__main__':

    start = dt.datetime.now()
    nums()
    print((dt.datetime.now() - start).microseconds)

    start = dt.datetime.now()
    origin()
    print((dt.datetime.now() - start).microseconds)
