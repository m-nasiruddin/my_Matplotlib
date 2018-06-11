#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 12:47:48 2018

@author: osboxes
"""

import matplotlib.pyplot as plt
from numpy.random import rand
a = rand(100)
print(a)
b = rand(100)
print(b)
plt.scatter(a, b)
plt.show()
