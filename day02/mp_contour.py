# _*_ coding : utf-8 _*_
# @Time: 2018/8/20 15:14
# @Author: Laurel-rao
# @Email: 13694846652@163.com

from matplotlib import pyplot as mp
import numpy as np

n = 1000
x, y = np.meshgrid(np.linspace(-3, 3, n),\
                    np.linspace(-3, 3, n))

z = (1 - x/2 + x**5 + y ** 3)*np.exp(-x ** 2 - y ** 2 )
mp.figure('Contour')

mp.grid(linestyle=':')
mp.contourf(x, y, z, 8, cmap='jet')
cntr = mp.contour(x, y, z, 8,colors='black', linewidths=0.5)

mp.clabel(cntr, inline_spacing=1, fmt='%.1f', fontsize=10)
mp.show()