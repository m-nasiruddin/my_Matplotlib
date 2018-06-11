#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 11:43:14 2018

@author: osboxes
"""

import matplotlib.pyplot as plt
import numpy as np
a = np.linspace(0, 10, 100)  # create an array with 100 equally spaced points
# starting with 0 and ending with 10
print(a)
b = np.exp(-a)
print(b)
plt.plot(a)
plt.show()
plt.plot(b)
plt.show()
plt.plot(a, b)
plt.show()
