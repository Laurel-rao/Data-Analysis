# _*_ coding : utf-8 _*_
# @Time: 2018/8/20 16:33
# @Author: Laurel-rao
# @Email: 13694846652@163.com

from matplotlib import pyplot as mp
import numpy as np

n = 1001
t = np.linspace(0, 2 * np.pi, n)
r_spiral = 0.8 * t
r_rose = 5 * np.sin(10 * t)



mp.figure('Polar')
mp.gca(projection='polar')

mp.title('Polar', fontsize=20)
mp.grid(linestyle=':')
mp.xlabel(r'$\theta$', fontsize=14)
mp.ylabel(r'$\rho$', fontsize=14)


mp.tick_params(labelsize=10)
# ax.plot_wireframe(x,y,z,rstride=30,cstride=30,linewidth=0.5,color='orangered')
mp.plot(t,r_rose,c='dodgerblue',label=r'$\rho = 5sin(6 \theta) $')
mp.plot(t,r_spiral,c='dodgerblue',label=r'$\rho = 0.8\theta) $', color='orangered')

mp.legend()
mp.show()