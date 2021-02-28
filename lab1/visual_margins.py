import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.01)
plt.plot(x, x ** 2, label=r'$f = x^2$')

plt.scatter(x, x ** 2 + np.random.randn(len(x)) * x, s=0.93)
plt.fill_between(x, 1.3 * x ** 2, 0.7 * x ** 2, alpha=0.71)

plt.legend(loc='upper left')
plt.savefig('figure_fill_between.png')
plt.show()

