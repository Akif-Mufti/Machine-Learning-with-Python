# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 16:02:08 2017

@author: user
"""
#KNeighborsRegressor
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_breast_cancer
import mglearn
try:
    from sklearn.datasets import train_test_split
except ImportError:
    from sklearn.cross_validation import train_test_split
x,y =mglearn.datasets.make_wave(n_samples=40)
# split the wave dataset into a training and a test set
x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=0) 
# Instantiate the model, set the number of neighbors to consider to 3:
reg= KNeighborsRegressor(n_neighbors=3)
#fit
reg.fit(x_train,y_train)
KNeighborsRegressor(algorithm='auto', leaf_size=30, metric='minkowski',
metric_params=None, n_jobs=1, n_neighbors=3, p=2,weights='uniform')

p=reg.predict(x_test)
s=reg.score(x_test,y_test)
fig, axes =plt.subplots(1,3,figsize=(15,4))
# create 1000 data points, evenly spaced between -3 and 3
line=np.linspace(-3,3,1000).reshape(-1,1)
plt.suptitle("Nearest_Neighbor_regression")
for n_neighbors, ax in zip([1,3,9],axes):
    # make predictions using 1, 3 or 9 neighbors
    reg = KNeighborsRegressor(n_neighbors=n_neighbors).fit(x, y)
    ax.plot(x, y, 'o')
    ax.plot(x, -3 * np.ones(len(x)), 'o')
    ax.plot(line, reg.predict(line))
    ax.set_title("%d neighbor(s)" % n_neighbors)
# Blue line is the respnse and the continious gree line is the prediction
#for linear regresson model
lrm =mglearn.plots.plot_linear_regression_wave()
    


 




