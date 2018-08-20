# _*_ coding : utf-8 _*_
# @Time: 2018/8/20 15:45
# @Author: Laurel-rao
# @Email: 13694846652@163.com

from matplotlib import pyplot as mp
import numpy as np




n = 1001
t = np.linspace(0, 2 * np.pi, n)
r_spiral = 0.8 * t



mp.figure('3D Surface')


mp.title('3D Surface', fontsize=20)
mp.grid(linestyle=':')
mp.xlabel(r'$\theta$', fontsize=14)
mp.ylabel(r'$\rho$', fontsize=14)


mp.tick_params(labelsize=10)
mp.pie([26,17,21,29,11],
    [0.05,0.01,0.01,0.01,0.01],
    ['Python', 'Java', 'C++', 'C', "PHP"],
    ['dodgerblue', 'orangered', 'limegreen','violet', 'gold'],
    '%d%%',
    shadow=True)
mp.legend()
mp.show()