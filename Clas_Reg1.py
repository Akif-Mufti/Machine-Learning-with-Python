# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 13:34:40 2017

@author: user
"""
#classification Example The color of the dot indicates its class, with red meaning class 0 and blue meaning class 1.
import mglearn 
import matplotlib.pyplot as plt
X, y = mglearn.datasets.make_forge()
plt.scatter(X[:, 0], X[:, 1], c=y, s=60, cmap=mglearn.cm2)
print("X.shape: %s" % (X.shape,))