#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 14:29:21 2018

@author: osboxes
"""

from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
ax = fig.gca(projection = '3d')
x = np.arange(-5, 5, 0.25)
y = np.arange(-5, 5, 0.25)
x, y = np.meshgrid(x, y)
r = np.sqrt(x**2 + y**2)
z = np.sin(r)
surf = ax.plot_surface(x, y, z, rstride = 1, cstride = 1, cmap = cm.coolwarm)
plt.show()
