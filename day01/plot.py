# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp

# 一条余弦曲线，一条正弦曲线

# 将-pi 到 pi 等分为 999 份，共1000个点
x = np.linspace(-np.pi, np.pi, 1000)
mp.figure(figsize=(10, 10))
# 获取纵坐标
cos_y = np.cos(x) / 2
sin_y = np.sin(x)
# 个性化设置
mp.xlim(x.min() * 1.2, x.max() * 1.2)
mp.ylim(sin_y.min() * 1.5, sin_y.max() * 1.5)
mp.yticks([-1, -0.5, 0,  0.5, 1])
mp.xticks([-np.pi, -np.pi * 3 / 4, -np.pi / 2.0, 0,
           np.pi / 2, np.pi * 3 / 4, np.pi],
          [r'$-\pi$', r'$-\frac{3}{4}\pi$', r'$-\frac{1}{2}\pi$',
           r'$0$', r'$\frac{1}{2}\pi$', r'$\frac{3}{4}\pi$', r'$\pi$'
           ])

asix = mp.gca()
asix.spines['left'].set_position(('data', 0))
asix.spines['bottom'].set_position(('data', 0))
asix.spines['top'].set_color('none')
asix.spines['right'].set_color('none')

xo = np.pi * 3 / 4
yo_cos = np.cos(xo) / 2
yo_sin = np.sin(xo)

mp.scatter([xo, xo], [yo_cos, yo_sin], s=60,
           edgecolor='limegreen', facecolor='white', zorder=3)
# 绘制图形
# mp.plot(x, cos_y, linestyle='--', linewidth=6, color='b')
# mp.plot(x, sin_y, linestyle=':', linewidth=0.5, color='g')
mp.plot(x, cos_y, label=r'$y=\frac{1}{2}cos(x)$')
mp.plot(x, sin_y, label=r'$y=sin(x)$')
mp.plot([xo, xo], [yo_cos, yo_sin], linestyle='--', color='limegreen')

mp.annotate(
    r'$sin(\frac{3\pi}{4})=\frac{\sqrt{2}}{2}$',
    xy=(xo, yo_sin),
    xycoords='data',
    xytext=(20, 20),
    textcoords='offset points',
    fontsize=12,
    arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2')
)

mp.annotate(
    r'$\frac{1}{2}cos(\frac{3\pi}{4})=-\frac{\sqrt{2}}{4}$',
    xy=(xo, yo_cos),
    xycoords='data',
    xytext=(-90, -40),
    textcoords='offset points',
    fontsize=12,
    arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2')
)
mp.legend(loc='upper left')
# 阻塞展示
mp.show()
