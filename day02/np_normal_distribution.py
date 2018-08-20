# _*_ coding : utf-8 _*_
# @Time: 2018/8/20 14:16
# @Author: Laurel-rao
# @Email: 13694846652@163.com

from matplotlib import pyplot as mp
import numpy as np

n = 1000
# 随机进行取数，按照正态分布进行排列
# σ（标准差，控制分散性，越大分散性小）
# μ（平均值）
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)

distance = np.sqrt(x**2 + y**2)
mp.figure('Scatter', facecolor='lightgray')
mp.title('Scatter', fontsize = 20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(x, y, s=60, c=distance,
           cmap='rainbow_r',   # 颜色映射
           alpha=0.5,
           marker='*'   # 'D' diamond, 's' square, '*' star, 'o'
           )

mp.show()
