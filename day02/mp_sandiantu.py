# _*_ coding : utf-8 _*_
# @Time: 2018/8/20 14:16
# @Author: Laurel-rao
# @Email: 13694846652@163.com

from matplotlib import pyplot as mp
import numpy as np
from mpl_toolkits.mplot3d import axes3d


n = 1000
# 随机进行取数，按照正态分布进行排列
# σ（标准差，控制分散性，越大分散性小）
# μ（平均值）
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)
z = np.random.normal(0, 1, n)


distance = np.sqrt(x**2 + y**2 + z**2)
mp.figure('Scatter3D', facecolor='lightgray')
ax = mp.gca(projection='3d')
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)
ax.set_zlabel('z', fontsize=14)
mp.title('Scatter', fontsize = 20)


mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
ax.scatter(x, y, z, s=60, c=distance,
           cmap='jet_r',   # 颜色映射
           alpha=0.5,
           marker='o'   # 'D' diamond, 's' square, '*' star, 'o'
           )

mp.show()
