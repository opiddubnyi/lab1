import pylab
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy


def makeData():
    x = numpy.arange(-10, 10, 0.1)
    y = numpy.arange(-10, 10, 0.1)
    xgrid, ygrid = numpy.meshgrid(x, y)
    zgrid = numpy.sin(xgrid) * numpy.sin(ygrid) / (xgrid * ygrid)
    return xgrid, ygrid, zgrid


x, y, z = makeData()

fig = pylab.figure()
axes = Axes3D(fig)
axes.plot_surface(x, y, z, rstride=4, cstride=4, cmap=cm.jet)
pylab.show()
