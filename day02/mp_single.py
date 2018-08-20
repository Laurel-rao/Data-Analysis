# _*_ coding : utf-8 _*_
# @Time: 2018/8/20 18:18
# @Author: Laurel-rao
# @Email: 13694846652@163.com

from matplotlib import pyplot as mp
import numpy as np
import matplotlib.animation as ma

mp.figure('Signal')
ax = mp.gca()

mp.xlabel('Time')
mp.ylabel('signal')
ax.set_ylim(-3, 3)
ax.set_xlim(0, 10)
mp.tick_params(labelsize=20)
mp.grid(linestyle=':')

pl = mp.plot([], [], c='orangered')[0]
pl.set_data([], [])

def update(data):
    t, v = data
    x, y = pl.get_data()
    x.append(t)
    y.append(v)
    min_x, max_x = ax.get_xlim()
    if t >= max_x:

        ax.set_xlim(t - (max_x - min_x), t)
        print(t - (min_x - max_x))
        # 使得画布进行重绘
        ax.figure.canvas.draw()
    pl.set_data(x, y)


def generator():
    t = 0
    while True:
        v = np.sin(2 * np.pi * t) * np.exp(
            np.sin(0.2 * np.pi *t)
        )

        yield t, v
        t += times

times = 0.05
ccc = ma.FuncAnimation(mp.gcf(), update, generator, interval=5)

mp.show()
