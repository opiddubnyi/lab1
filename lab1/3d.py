from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

ax = axes3d.Axes3D(plt.figure())
i = np.arange(-1, 1, 0.01)

X, Y = np.meshgrid(i, i)
Z = X**2 - Y**2

ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

plt.show()


# IQ histogram

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)
# the histogram of the data

n, bins, patches = plt.hist(x, 50, density=True, facecolor='g', alpha=0.75)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .030, r'$\mu=100,\ \sigma=15$')
plt.text(50, .033, r'$\varphi_{\mu,\sigma^2}(x) = \frac{1}{\sigma\sqrt{'
                   r'2\pi}} \,e^{ -\frac{(x- \mu)^2}{2\sigma^2}} = \frac{1}{'
                   r'\sigma} \varphi\left(\frac{x - \mu}{\sigma}\right),'
                   r'\quad x\in\mathbb{R}$', fontsize=20, color='red')
plt.axis([40, 160, 0, 0.04])
plt.grid(True)
plt.show()

# pie chart

data = [33, 245, 20, 12, 10]
plt.figure(num=1, figsize=(6, 6))
plt.axes(aspect=1)
plt.title('Plot 3', size=14)
plt.pie(data, labels=('Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5'))
plt.show()