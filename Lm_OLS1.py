# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 16:02:08 2017

@author: user
"""
#Linear Model Ordinary Least Square
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt
import numpy as np

import mglearn
try:
    from sklearn.datasets import train_test_split
except ImportError:
    from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
x,y= mglearn.datasets.load_extended_boston()
x_train,x_test,y_train,y_test = train_test_split(x,y,random_state = 0)
lr=LinearRegression().fit(x_train,y_train)
print("lr.coef_: %s" % lr.coef_)
print("lr.intercept_: %s" % lr.intercept_)
print("training set score: %f" % lr.score(x_train, y_train))
print("test set score: %f" % lr.score(x_test, y_test))

#In this case we will witness very different  test and training score, it is overfitting .
 




