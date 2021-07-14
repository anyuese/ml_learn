import math
import random
import re
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from icecream import ic
from pylab import mpl
from collections import defaultdict
from matplotlib.colors import BASE_COLORS
colors = list(BASE_COLORS.values())

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

coordination_source = """
{name:'兰州', geoCoord:[103.73, 36.03]},
{name:'嘉峪关', geoCoord:[98.17, 39.47]},
{name:'西宁', geoCoord:[101.74, 36.56]},
{name:'成都', geoCoord:[104.06, 30.67]},
{name:'石家庄', geoCoord:[114.48, 38.03]},
{name:'拉萨', geoCoord:[102.73, 25.04]},
{name:'贵阳', geoCoord:[106.71, 26.57]},
{name:'武汉', geoCoord:[114.31, 30.52]},
{name:'郑州', geoCoord:[113.65, 34.76]},
{name:'济南', geoCoord:[117, 36.65]},
{name:'南京', geoCoord:[118.78, 32.04]},
{name:'合肥', geoCoord:[117.27, 31.86]},
{name:'杭州', geoCoord:[120.19, 30.26]},
{name:'南昌', geoCoord:[115.89, 28.68]},
{name:'福州', geoCoord:[119.3, 26.08]},
{name:'广州', geoCoord:[113.23, 23.16]},
{name:'长沙', geoCoord:[113, 28.21]},
//{name:'海口', geoCoord:[110.35, 20.02]},
{name:'沈阳', geoCoord:[123.38, 41.8]},
{name:'长春', geoCoord:[125.35, 43.88]},
{name:'哈尔滨', geoCoord:[126.63, 45.75]},
{name:'太原', geoCoord:[112.53, 37.87]},
{name:'西安', geoCoord:[108.95, 34.27]},
//{name:'台湾', geoCoord:[121.30, 25.03]},
{name:'北京', geoCoord:[116.46, 39.92]},
{name:'上海', geoCoord:[121.48, 31.22]},
{name:'重庆', geoCoord:[106.54, 29.59]},
{name:'天津', geoCoord:[117.2, 39.13]},
{name:'呼和浩特', geoCoord:[111.65, 40.82]},
{name:'南宁', geoCoord:[108.33, 22.84]},
//{name:'西藏', geoCoord:[91.11, 29.97]},
{name:'银川', geoCoord:[106.27, 38.47]},
{name:'乌鲁木齐', geoCoord:[87.68, 43.77]},
{name:'香港', geoCoord:[114.17, 22.28]},
{name:'澳门', geoCoord:[113.54, 22.19]}
"""

def get_city_info(coordination_source):
    city_location = dict()
    test_string = "{name:'兰州', geoCoord:[103.73, 36.03]},"
    pattern = re.compile(r"name:'(\w+)',\s+geoCoord:\[(\d+.\d+),\s(\d+.\d+)\]")

    for line in coordination_source.split('\n'):
        city_info = pattern.findall(line)
        if not city_info: continue

        city, long, lat = city_info[0]
        long, lat = float(long), float(lat)
        city_location[city] = (long, lat)
    return city_location


def get_geo_distance(origin, destination):
    """
    Calculate the Haversine distance.

    Parameters
    ----------
    origin : tuple of float
        (lat, long)
    destination : tuple of float
        (lat, long)

    Returns
    -------
    distance_in_km : float

    Examples
    --------
    >>> origin = (48.1372, 11.5756)  # Munich
    >>> destination = (52.5186, 13.4083)  # Berlin
    >>> round(distance(origin, destination), 1)
    504.2
    """
    lon1, lat1 = origin
    lon2, lat2 = destination
    radius = 6371  # km

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c

    return d


def show_init_data(city_location):
    city_graph = nx.Graph()
    city_graph.add_nodes_from(list(city_location.keys()))
    nx.draw(city_graph, city_location, with_labels=True, node_size=30)
    plt.pause(0.1)


def get_random_center(points):
    coo_x_s, coo_y_s = [coordinate[0] for coordinate in points], [coordinate[1] for coordinate in
                                                                       points]
    return (random.uniform(min(coo_x_s), max(coo_x_s)), random.uniform(min(coo_y_s), max(coo_y_s)))


def get_mean_center(points):
    # ic(points)
    all_x, all_y = [x for x, y in points], [y for x, y in points]
    return (np.mean(all_x), np.mean(all_y))


def kmeans(k,points,centers=None):
    if not centers: centers = [get_random_center(points) for i in range(k)]

    # step1 将数据分成k个簇
    close_neighbor = defaultdict(set)
    for p in points:
        close_center = min(centers,key=lambda c:get_geo_distance(c,p))
        close_neighbor[close_center].add(tuple(p))
    # ic(close_neighbor)
    plot_result(close_neighbor)
    # step2 计算k个簇的中心
    new_centers = list()
    for c, p in close_neighbor.items():
        new_center = get_mean_center(p)
        new_centers.append(new_center)
    
    # step3 若中心点变化很大，则继续调用keamns
    threshold = 1
    distances = [get_geo_distance(p1,p2) for p1,p2 in zip(centers,new_centers)]
    ic(distances)
    if all(d>1 for d in distances):
        kmeans(k,points,new_centers)
    return close_neighbor,new_centers

def plot_result(close_neighbor):
    plt.cla()
    i = 0
    for c,p in close_neighbor.items():
        plt.scatter(c[0],c[1],marker='*',c=colors[i])
        plt.scatter([x for x,y in p], [y for x,y in p], c=colors[i])
        i += 1
    plt.pause(1)

def draw_city(city_info,color=None):
    graph = nx.Graph()
    graph.add_nodes_from(list(city_info.keys()))
    nx.draw(graph,city_info,node_color=color,node_size=30,with_labels=True)

city_location = get_city_info(coordination_source)
points = [value for key, value in city_location.items()]
close_neighbor, centers = kmeans(4,points)
centers_d = dict(enumerate(centers))
ic(close_neighbor)
ic(centers_d)

# 清空画布
plt.clf()
draw_city(city_location)
draw_city(centers_d)