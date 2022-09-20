# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection  # appropriate import to draw 3d polygons


plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
plt.xlim(20)
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)

x, y = np.meshgrid(x, y)
eq = 0.12 * x + 0.01 * y + 1.09

fig = plt.figure()

x1=np.array([-4, 1, 6])
y1=np.array([0, 5, 0])
z1=np.array([0, 0, 2])  # z1 should have 3 coordinates, right?


ax = fig.gca(projection='3d')

# 1. create vertices from points
verts = [list(zip(x1, y1, z1))]
# 2. create 3d polygons and specify parameters
srf = Poly3DCollection(verts, alpha=.25, facecolor='#800000')
ax.plot_surface(x, y, eq)
ax.add_collection3d(srf)
plt.show()