import numpy as np
from icecream import ic
import matplotlib.pyplot as plt

X = np.random.normal(size=(10, 7))
y = np.array([
    [1],
    [0],
    [0],
    [0],
    [1],
    [0],
    [0],
    [1],
    [0],
    [0],
])

weights = np.random.normal(size=(1, 7))
bias = 0


def loss(y_hat, y):
    return np.mean((y_hat - y) ** 2)


def patial_w(y_hat, y, X):
    ic(y_hat.shape,y.shape,X.shape)
    return 2 * np.mean((y_hat - y) * X, axis=0)


def patial_b(y_hat, y):
    return 2 * np.mean(y_hat - y)


def linear_fuc(w, X, b):
    y_hat = X @ w + b
    return y_hat

def logistic(x):
    return 1/(1 + np.exp(x))

def cross_entropy(y_hat,y):
    return np.mean(y*np.log(y_hat))

def softmax(x):
    x -= np.max(x)
    sum_ = np.sum(np.exp(x))

    return np.exp(x) / sum_


def linear_regression_example(weights,X,y,bias):
    learning_rate = 2 * (1e-3)
    loss_sl = list()
    probs = list()
    for i in range(100):
        y_hat = linear_fuc(weights.T, X, bias)
        # ic(y_hat)
        loss_ = loss(y_hat, y)
        loss_sl.append(loss_)
        weights -= patial_w(y_hat, y, X) * learning_rate
        ic(weights.shape)
        bias -= patial_b(y_hat, y)
        ic(loss_)
        prob = np.array((y_hat > 0.5), dtype=int)
        ic(prob)
    plt.plot(loss_sl)
    plt.show()
    ic(probs)

def logistic_regression_example():
    learning_rate = 2 * (1e-3)
    loss_sl = list()
    probs = list()
    for i in range(100):
        x = linear_fuc(weights.T, X, bias)
        y_hat = logistic(x)
        ic(y_hat)
        loss_ = loss(y_hat, y)
        loss_sl.append(loss_)
        weights -= patial_w(y_hat, y, X) * learning_rate
        ic(weights.shape)
        bias -= patial_b(y_hat, y)
        ic(loss_)
        prob = np.array((y_hat > 0.5), dtype=int)
        ic(prob)
    plt.plot(loss_sl)
    plt.show()
    ic(probs)


if __name__ == '__main__':
    linear_regression_example(weights,X,y,bias)


