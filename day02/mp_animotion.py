# _*_ coding : utf-8 _*_
# @Time: 2018/8/20 17:26
# @Author: Laurel-rao
# @Email: 13694846652@163.com

from matplotlib import pyplot as mp
import numpy as np
import matplotlib.animation as ma

n_bubbles = 100
# indexs
# position(float)
# size(float)
# growth(float)
# color(r 0-1,g 0-1,b 0-1, alpha float)

bubbles = np.zeros(n_bubbles, dtype=[
    ('position', float, 2),
    ('size', float, 1),    # 大小
    ('growth', float, 1),  # 增长速度
    ('color', float, 4)    # 颜色， rgb 和 透明度
])

bubbles['position'] = np.random.uniform(0, 1, (n_bubbles, 2))
bubbles['size'] = np.random.uniform(50, 750, n_bubbles)
bubbles['color'] = np.random.uniform(0, 1, (n_bubbles, 4))
bubbles['growth'] = np.random.uniform(30, 150, n_bubbles)
mp.figure('Bubbles', facecolor='lightgray')
mp.xticks(())
mp.yticks(())

sc = mp.scatter(bubbles['position'][:, 0],
               bubbles['position'][:, 1],
               s = bubbles['size'],
               c = bubbles['color']
               )

def update(number):

    print('number==%s'%number)
    bubbles['size'] += bubbles['growth']
    burst = number % n_bubbles
    bubbles['position'][burst] = np.random.uniform(0,1,2)
    bubbles['size'][burst] = 0
    bubbles['growth'][burst]=\
        np.random.uniform(30,150)
    bubbles['color'][burst] = \
        np.random.uniform(0,1,4)
    sc.set_offsets(bubbles['position'])
    sc.set_sizes(bubbles['size'])
    sc.set_facecolors(bubbles['color'])


sm = ma.FuncAnimation(mp.gcf(), update, interval=10)


mp.show()

