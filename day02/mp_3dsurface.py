# _*_ coding : utf-8 _*_
# @Time: 2018/8/20 16:12
# @Author: Laurel-rao
# @Email: 13694846652@163.com

from matplotlib import pyplot as mp
import numpy as np
from mpl_toolkits.mplot3d import axes3d

n = 1000

n = 1000
x, y = np.meshgrid(np.linspace(-3, 3, n),\
                    np.linspace(-3, 3, n))

z = (1 - x/2 + x**5 + y ** 3)*np.exp(-x ** 2 - y ** 2 )
mp.figure('3D Surface')

ax = mp.gca(projection='3d') # Unknown projection '3d'
mp.title('3D Surface', fontsize=20)
mp.grid(linestyle=':')
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)
ax.set_zlabel('z', fontsize=14)

mp.tick_params(labelsize=10)
# ax.plot_wireframe(x,y,z,rstride=30,cstride=30,linewidth=0.5,color='orangered')
ax.plot_surface(x,y,z,rstride=10,cstride=10,cmap='jet')

mp.show()