# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 15:18:22 2017

@author: user
"""
#knn
import mglearn
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
boston = load_boston()
print(boston.data.shape)
##This derived dataset can be loaded using the load_extended_boston function:
X, y = mglearn.datasets.load_extended_boston()
print(X.shape)
mglearn.plots.plot_knn_classification(n_neighbors=3)
plt.title("forge_one_neighbor");