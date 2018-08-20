# _*_ coding : utf-8 _*_
# @Time: 2018/8/20 9:37
# @Author: Laurel-rao
# @Email: 13694846652@163.com

from matplotlib import pyplot as mp
import numpy as np

# 表示x轴的数组
x = np.linspace(-np.pi, np.pi, 1000)
# 表示曲线y轴的数组
cos_y = np.cos(x) / 2
sin_y = np.sin(x)

mp.figure('Sin', figsize=(6,4), dpi=120, \
            facecolor='dodgerblue', edgecolor='limegreen')

mp.title('Sin', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y=Sin(x)', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=":")

mp.figure('Cos', figsize=(6,4), dpi=120, \
            facecolor='dodgerblue', edgecolor='limegreen')

mp.title('Cos', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel(r'$y=\frac{1}{2}Cos(x)$', fontsize=14)
#
mp.tick_params(labelsize=10)
# 设置网格线
mp.grid(linestyle=":")




mp.figure('Sin')
mp.plot(x, sin_y, c='orangered', label=r'$y=Sin(x)$')
# 设置图例的标签
mp.legend()




mp.figure('Cos')
mp.plot(x, cos_y, c='orangered', label=r'$y=\frac{1}{2}Cos(x)$')
mp.legend()


mp.show()
