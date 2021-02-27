import numpy as np

x1 = [1, 10, 100]


def y(x):
    return np.log(
        (np.exp((1 / (np.sin(x) + 1)))) / (5 / 4 + 1 / x ** 15)) / \
           np.log(1 + x ** 2)


for i in x1:
    print(y(i))

