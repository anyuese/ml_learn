from collections import Counter
import numpy as np
import pandas as pd
from icecream import ic
from sklearn.datasets import load_iris

iris_x = load_iris()['data']
iris_y = load_iris()['target']

ic(iris_x)
ic([6.2,1.2,4.6,2.3] in iris_x)
ic(iris_y)


def knn(x, y,query, k=3, clf=True):
    history = {tuple(x_):y_ for x_,y_ in zip(x, y)}
    neighbors = sorted(history.items(),key=lambda x:np.sum((np.array(x[0])-np.array(query))**2))
    counter = Counter(neighbors)
    neighbors_y = [y for x,y in neighbors]
    if clf: return counter.most_common()[0][0]
    else: return np.mean(neighbors_y)

knn(iris_x,iris_y,[6.2,1.2,4.6,2.3])




def get_pro(elements):
    counter = Counter(elements)
    pr = np.array([counter[e] / len(elements) for e in elements])
    return pr


def gini(elements):
    pr = get_pro(elements)
    return 1 - np.sum(pr ** 2)


def entropy(elements):
    pr = get_pro(elements)
    return -np.sum(pr * np.log2(pr))


def cart_loss(left, right, pure_fn):
    m_left, m_right = len(left), len(right)
    m = m_left + m_right

    return m_left / m * pure_fn(left) + m_right / m * pure_fn(right)


sales = {
    'gender': ['Female', 'Female', 'Female', 'Female', 'Male', 'Male', 'Male'],
    'income': ['H', 'M', 'H', 'M', 'H', 'H', 'L'],
    'family-number': [1, 1, 2, 1, 1, 1, 2],
    'bought': [1, 1, 1, 0, 0, 0, 1]
}

data = pd.DataFrame.from_dict(sales)
target = 'bought'


def find_best_split(training_data, target):
    training_data = training_data
    mini_loss = float('inf')

    fields = set(training_data.columns.tolist()) - {target}
    best_splite, best_loss = None, None

    for x in fields:
        field_values = training_data[x]
        for v in field_values:
            split_left = training_data[training_data[x] == v][target].tolist()
            split_right = training_data[training_data[x] != v][target].tolist()

            loss = cart_loss(split_left, split_right, gini)
            if loss < mini_loss: mini_loss = loss
