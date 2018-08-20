# _*_ coding : utf-8 _*_
# @Time: 2018/8/20 16:12
# @Author: Laurel-rao
# @Email: 13694846652@163.com

from matplotlib import pyplot as mp
import numpy as np
from mpl_toolkits.mplot3d import axes3d


y = np.array([1,10,100,1000,100,10,1])
mp.figure('Normal & log', facecolor='lightgray')
mp.subplot(211)
mp.title('Normal', fontsize=16)
mp.ylabel('y', fontsize=16)

ax = mp.gca()
ax.xaxis.set_major_locator(
    mp.MultipleLocator(1)
)
ax.xaxis.set_minor_locator(
    mp.MultipleLocator(0.1)
)
ax.yaxis.set_major_locator(
    mp.MultipleLocator(250)
)
ax.yaxis.set_minor_locator(
    mp.MultipleLocator(50)
)
mp.tick_params(labelsize=10)
mp.grid(which='major', axis='both', linewidth=0.75, linestyle='-',
        color='lightgray')

mp.grid(which='major', axis='both', linewidth=0.25, linestyle='-',
        color='lightgray')

mp.semilogy(y, 'o-', c='dodgerblue', label='plot')
mp.legend()



mp.show()