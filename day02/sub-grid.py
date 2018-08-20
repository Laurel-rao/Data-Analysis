# _*_ coding : utf-8 _*_
# @Time: 2018/8/20 10:10
# @Author: Laurel-rao
# @Email: 13694846652@163.com

from matplotlib import pyplot as mp
import numpy as np
import matplotlib.gridspec as mg

mp.figure('GridSpec', facecolor='lightgray')
gs = mg.GridSpec(3, 2)
mp.subplot(gs[0, :2])
mp.xticks(())
mp.yticks(())
mp.text(0.5, 0.5, '1', ha='center', va='center', size=36, alpha=0.5)

mp.subplot(gs[1:, 0])
mp.xticks(())
mp.yticks(())
mp.text(0.5, 0.5, '2', ha='center', va='center', size=36, alpha=0.5)

mp.subplot(gs[1, 1])
mp.xticks(())
mp.yticks(())
mp.text(0.5, 0.5, '3', ha='center', va='center', size=36, alpha=0.5)

mp.subplot(gs[2, 1])
mp.xticks(())
mp.yticks(())
mp.text(0.5, 0.5, '4', ha='center', va='center', size=36, alpha=0.5)

mp.tight_layout()
mp.show()