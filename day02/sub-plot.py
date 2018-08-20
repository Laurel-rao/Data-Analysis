# _*_ coding : utf-8 _*_
# @Time: 2018/8/20 10:03
# @Author: Laurel-rao
# @Email: 13694846652@163.com

from matplotlib import pyplot as mp
import numpy as np

# mp.figure('Subplot',figsize=(4, 4), facecolor='gray', dpi=200)
# mp.subplot(221)
# mp.xticks(())
# mp.yticks(())
# mp.text(0.5, 1, '1', ha='right', va='top', size=36, alpha=0.5)
#
#
#
# mp.subplot(222)
# mp.xticks(())
# mp.yticks(())
# mp.text(0.5, 0.5, '2', ha='center', va='center', size=36, alpha=0.5)
#
#
# mp.subplot(223)
# mp.xticks(())
# mp.yticks(())
# mp.text(0.5, 0.5, '3', ha='center', va='center', size=36, alpha=0.5)
#
#
# mp.subplot(224)
# mp.xticks(())
# mp.yticks(())
# mp.text(0.5, 0.5, '4', ha='center', va='center', size=36, alpha=0.5)


mp.figure(facecolor='lightgray')
# 一共有两行
for i in range(2):
    # 一共有三列
    for j in range(3):
        k = i * 3 + j + 1
        mp.subplot(2, 3, k)
        # 设置刻度为无刻度
        mp.xticks(())
        mp.yticks(())
        mp.text(0.5,  # 文字中心在图像的位置，使用比例
                0.5,  # 文字在图像的位置，使用比例
                '%d'%k,  # 文字
                ha='center',  # 相对于窗口中心的位置 'center', 'right', 'left'
                va='center',  # 取值为'top', 'bottom', 'center', 'baseline'
                size=36,  # 文字的大小
                alpha=0.5  # 文字的透明度
                )


mp.tight_layout()
mp.show()