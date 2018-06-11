#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 12:35:56 2018

@author: osboxes
"""

import matplotlib.pyplot as plt
from numpy.random import normal
x = normal(size = 200)
plt.hist(x, bins = 30)
plt.show()
