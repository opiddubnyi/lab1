import numpy as np
import matplotlib.pyplot as plt


def quad():
    x = np.arange(-15, 15, 0.01)
    plt.plot(x, x ** 2 - x - 6)
    plt.plot(-2, 0, 'ro', 3, 0, 'ro')
    plt.grid(True)

    plt.show()


data = []
data_labels = []

with plt.xkcd():
    for i in range(int(input())):

        data.append(int(input()))
        data_labels.append(str(input()))

    plt.pie(data, labels=data_labels)
    plt.title('Где ведутся самые ожесточенные бои')

    plt.show()

