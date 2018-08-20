# _*_ coding : utf-8 _*_
# @Time: 2018/8/20 10:19
# @Author: Laurel-rao
# @Email: 13694846652@163.com

from matplotlib import pyplot as mp
import numpy as np

mp.figure('Axes', facecolor='lightgray')
mp.axes([0.03, 0.038, 0.94, 0.924])
mp.xticks(())
mp.yticks(())
mp.text(0.5, 0.5, '1', ha='center', va='center', size=36, alpha=0.5)

mp.figure('Axes', facecolor='lightgray')
mp.axes([0.63, 0.076, 0.31, 0.308])
mp.xticks(())
mp.yticks(())
mp.text(0.5, 0.5, '2', ha='center', va='center', size=36, alpha=0.5)
mp.show()

