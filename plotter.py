from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np


def get_key(i, j):
    return '{}_{}'.format(i, j)


def fun(i, j):
    return Zf[get_key(i, j)]


X, Y, Zf = [], [], {}
with open('result.tsv') as f:
    for line in list(f.readlines()):
        l = line.split()
        i = int(l[0])
        j = int(l[1])
        X.append(i)
        Y.append(j)
        Zf[get_key(i, j)] = (float(l[2]))


X, Y = np.meshgrid(X, Y)

zs = np.array([fun(x, y) for x, y in zip(np.ravel(X), np.ravel(Y))])
Z = zs.reshape(X.shape)

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
# ax.set_zlim(-1.01, 1.01)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)
plt.title('Original Code')
plt.show()