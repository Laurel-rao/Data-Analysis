# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np

a = np.array([
    [1 + 1j, 2 + 4j, 3 + 7j],
    [4 + 2j, 5 + 5j, 6 + 8j],
    [7 + 3j, 8 + 6j, 9 + 9j],
])
# b = a.shape()
# 数组属性
print(a.dtype, a.dtype.str, a.dtype.char)
# 数组形状（各维度值，从大到小）
print(a.shape)
# 维度数量
print(a.ndim)
# 大小，元素的数量
print(a.size, len(a))
# 数组中元素的大小，以字节为单位
print(a.itemsize)
# 数组总体的大小，以字节为单位
print(a.nbytes)
# 数据进行转换后，生成一个新的形状的数组，按照线性代数进行转换
print(a.T)
# 复数的实部
print(a.real)
# 复数的虚部
print(a.imag)
# 扁平迭代器
for item in a.flat:
    print(item)
