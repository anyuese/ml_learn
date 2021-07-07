from collections import defaultdict

import matplotlib.pyplot as plt
import numpy as np
from icecream import ic
from matplotlib.colors import BASE_COLORS

point = np.random.normal(loc=1, size=(100, 2))
point1 = np.random.normal(loc=2, size=(100, 2))
point2 = np.random.normal(loc=3, size=(100, 2))
point3 = np.random.normal(loc=4, size=(100, 2))
point4 = np.random.normal(loc=5, size=(100, 2))

points = np.concatenate([point, point1, point2, point3, point4])
# plt.scatter(points[:,0],points[:,1])
# plt.show()
ic(points)
k = 4


# 随机取K个分类中心
def random_center(k, points):
    for i in range(k):
        yield np.random.choice(points[:, 0]), np.random.choice(points[:, 1])


# 计算各个点的中心点
def mean(points):
    all_x, all_y = [x for x,y in points], [y for x,y in points]
    return np.mean(all_x), np.mean(all_y)


# 计算两点之间的距离
def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def kmeans(k, points, centers=None):
    # 取中心
    colors = list(BASE_COLORS)
    if not centers: centers = list(random_center(k, points))
    ic(centers)

    # 画出未分类前的中心以及图像
    # print(list())
    # for i, c in enumerate(centers):
    #     print(i, c)
    #     plt.scatter([c[0]], [c[1]], c=colors[i], marker='*')
    # plt.scatter(points[:, 0], points[:, 1], c='black')
    # plt.show()

    # 开始分类 step 1: 计算每个点离得最近的中心点,将数据分为K个簇
    center_neighbor = defaultdict(set)
    for p in points:
        close_c = min(centers, key=lambda c: distance(p, c))
        center_neighbor[close_c].add(tuple(p))

    # ic(center_neighbor)
    # 画出划分簇后的图像
    for i, c in enumerate(center_neighbor):
        _points = center_neighbor[c]
        all_x, all_y = [x for x, y in _points], [y for x, y in _points]
        plt.scatter(all_x, all_y, c=colors[i])
        plt.scatter(c[0], c[1], marker='*')

    plt.show()

    # step 2： 重新计算每个分类的中心
    new_centers = []
    for c in center_neighbor:
        new_center = mean((center_neighbor[c]))
        new_centers.append(new_center)

    # step 3: 计算旧的中心和新中心的距离
    distances = []
    distances = [distance(p1, p2) for p1, p2 in zip(centers, new_centers)]
    ic(distances)


    # step 4:给定阈值thresold, 若center和new_center距离大于thresold,则继续调用kmeans
    thresold = 1
    if all(d < thresold for d in distances):
        return center_neighbor
    else:
        kmeans(k, points, new_centers)


kmeans(k, points)
