# _*_ coding : utf-8 _*_
# @Time: 2018/8/20 14:33
# @Author: Laurel-rao
# @Email: 13694846652@163.com

from matplotlib import pyplot as mp
import numpy as np

n = 1000
y = np.random.normal(0,1,n)
x = np.linspace(0, 8*np.pi, n)
sin_y = np.sin(x)
cos_y = np.cos(x/2) /2
mp.figure('Fill', facecolor='lightgray')
mp.title('Fill', fontsize=20)
mp.xlabel('x', fontsize=10)
mp.ylabel('y', fontsize=10)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(x, sin_y, c='dodgerblue', label=r'$y=sin(x)$')
mp.plot(x, cos_y, c='orangered', label=r'$y=\frac{1}{2}cos(\frac{x}{2})$')

mp.fill_between(x, cos_y, sin_y,where=sin_y > cos_y, color='gray', alpha=0.5)
mp.fill_between(x, cos_y, sin_y,where=sin_y < cos_y, color='orangered', alpha=0.5)

mp.legend()
mp.show()