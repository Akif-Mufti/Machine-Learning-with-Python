# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 14:39:08 2017

@author: user
"""

import mglearn 
import matplotlib.pyplot as plt
import numpy as np 
X, y = mglearn.datasets.make_wave(n_samples=40)
plt.plot(X, y, 'o')
plt.plot(X, -3 * np.ones(len(X)), 'o')
plt.ylim(-3.1, 3.1)


