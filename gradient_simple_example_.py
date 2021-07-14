import random
import time
import matplotlib.pyplot as plt
import numpy as np
from icecream import ic

# 定义loss 函数
def loss(x, w, b, y):
    return ((w * x + b) - y) ** 2

# 定义w的偏导
def patial_w(x, w, b, y):
    return 2 * ((w * x + b) - y) * x

# 定义b的偏导
def patial_b(x, w, b, y):
    return 2 * ((w * x + b) - y)


w, b = random.randint(-10, 10), random.randint(-10, 10)

x, y = 10, 0.35
alpha = 1e-3
for i in range(100):
    w = w + -1 * patial_w(x, w, b, y)*alpha
    b -= patial_b(x, w, b, y)
    ic(loss(x, w, b, y))
    x_l = np.linspace(0, 13, 100)

    # 可视化查看效果
    if i%4 ==0:
        plt.clf()
        plt.plot(x_l, w * x_l + b, c='black')
        plt.scatter(x, y, marker="*", c='red')
        plt.text(1, 4, 'Loss={0}'.format(loss(x, w, b, y)), fontdict={'size': 10, 'color': 'red'})
        plt.pause(0.1)



