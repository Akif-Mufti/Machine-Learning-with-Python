# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 16:49:49 2017

@author: user
"""
#Linear model regression and linear support Vector Machine
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
import matplotlib.pyplot as plt
import mglearn
#try:
#    from sklearn.datasets import train_test_split
#except ImportError:
#    from sklearn.cross_validation import train_test_split
X,y = mglearn.datasets.make_forge()
fix,axes = plt.subplots(1,2,figsize=(10,3))
plt.suptitle("Linear_Classifiers")
for model,ax in zip([LinearSVC(),LogisticRegression()],axes):
    clf = model.fit(X,y)
    mglearn.plots.plot_2d_separator(clf,X,fill =False,eps=0.5,ax=ax,alpha=0.7)
    ax.scatter(X[:,0],X[:,1],c=y,s=100, cmap=mglearn.cm2)
    ax.set_title("%s"%clf.__class__.__name__)
mglearn.plots.plot_linear_svc_regularization()

