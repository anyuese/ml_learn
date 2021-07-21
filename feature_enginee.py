import numpy as np
from icecream import ic
from matplotlib import pyplot as plt
from sklearn.preprocessing import OneHotEncoder
from sklearn import preprocessing
import seaborn as sns




def standarized(x):
    return (x - np.mean(x)) / np.std(x)


def normalization(x):
    return (x - np.min(x)) / (np.max(x) - np.min(x))


def test_normalization():
    feature = np.random.uniform(10, 100, 20)
    plt.scatter(range(20), feature, c='red')
    plt.show()
    plt.clf()
    plt.scatter(range(20), normalization(feature), c='blue')
    plt.show()


def test_standarized():
    feature = np.random.uniform(10, 100, 40)
    plt.plot(feature, c='red')
    plt.show()
    plt.clf()
    plt.plot(standarized(feature), c='blue')
    plt.show()

def one_hot(element):
    es = list(set(element))
    for i in element:
        l = [0 for i in range(len(es))]
        l[es.index(i)] = 1
        print(l)

one_hot(['巴黎', '东京', '山东', '上海','巴黎'])

encoder = OneHotEncoder()
encoder.fit(np.array(['巴黎', '东京', '山东', '上海','巴黎']).reshape(-1,1))
ic(encoder.transform([['山东']]).toarray())
ic(encoder.inverse_transform([[0,1,0,0]]))

def test_preprocess_data():
    weight = np.random.normal(loc=80,scale=100,size=1000).reshape(-1,1)
    height = np.random.normal(loc=160,scale=60,size=1000).reshape(-1,1)
    original_data = np.concatenate((weight,height),axis=1)
    return original_data
    # ic(original_data,original_data.shape)

def plot(data,title):
    sns.set_style('dark')
    fig,ax = plt.subplots()
    ax.set(xlabel='height(blue)/weight(red)')
    ax.set(ylabel='frequency')
    ax.set(title=title)
    sns.displot(data[:,0],color='red',ax=ax,kde=True)
    sns.displot(data[:,1],color='blue',ax=ax,kde=True)
    plt.show()

original_data = test_preprocess_data()

standarized_data = preprocessing.StandardScaler().fit_transform(original_data)
plot(standarized_data,'StandardScaler')

mini_max_scaler_data = preprocessing.MinMaxScaler().fit_transform(original_data)
plot(mini_max_scaler_data, 'MinMaxScaler')

normal_scaler_data = preprocessing.Normalizer().fit_transform(original_data)
plot(standarized_data, 'NormalScaler')

robust_scaler_data = preprocessing.RobustScaler().fit_transform(original_data)
plot(standarized_data, 'RobustScaler')







    # ic(weight,height)

# test_normalization2()
test_preprocess_data()
# test_normalization()
# test_standarized()
