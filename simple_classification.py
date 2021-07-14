from torchvision.datasets import MNIST
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from icecream import ic

train = MNIST('dataset',train=True,download=True)
test = MNIST('dataset',train=False,download=True)

# print(train)
# print(test)

train_zero_and_six = [t for i,t in enumerate(train) if train.targets[i] in [0,6]]
test_zero_and_six = [t for i,t in enumerate(test) if test.targets[i] in [0,6]]

# ic(train_zero_and_six)
# ic(test_zero_and_six)
ic(np.array(train_zero_and_six[0][0]).reshape(-1,))

zero_and_six_train_x = np.array([np.array(t).reshape(-1,) for t,label in train_zero_and_six])
zero_and_six_test_x = np.array([np.array(t).reshape(-1,) for t,label in test_zero_and_six])
ic(zero_and_six_train_x.shape)

zero_and_six_train_y = np.array([label for t,label in train_zero_and_six])
zero_and_six_test_y = np.array([label for t,label in test_zero_and_six])

lr_model = LogisticRegression(solver='lbfgs',max_iter=1000)
lr_model.fit(zero_and_six_train_x,zero_and_six_train_y)

for i in range(5):
    index = np.random.choice(range(len(zero_and_six_test_x)))
    ic(lr_model.predict([zero_and_six_test_x[index]]))
    plt.imshow(zero_and_six_test_x[index].reshape(28,28))
    plt.show()

ic(lr_model.score(zero_and_six_train_x,zero_and_six_train_y))
ic(lr_model.score(zero_and_six_test_x,zero_and_six_test_y))


ic(lr_model.intercept_)

#
plt.imshow(lr_model.coef_.reshape(28,28))
plt.show()







