# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 16:02:08 2017

@author: user
"""
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

import mglearn


try:
    from sklearn.datasets import train_test_split
except ImportError:
    from sklearn.cross_validation import train_test_split
    
X, y = mglearn.datasets.make_forge()
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train, y_train)
KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',metric_params=None, n_jobs=1, n_neighbors=3, p=2,weights='uniform')
a=clf.predict(X_test)
b=clf.score(X_test, y_test)
fig, axes = plt.subplots(1, 3, figsize=(10, 3))
for n_neighbors, ax in zip([1, 3, 9], axes):
    clf = KNeighborsClassifier(n_neighbors=n_neighbors).fit(X, y)
    mglearn.plots.plot_2d_separator(clf, X, fill=True, eps=0.5, ax=ax, alpha=.4)
    ax.scatter(X[:, 0], X[:, 1], c=y, s=60, cmap=mglearn.cm2)
    ax.set_title("%d neighbor(s)" % n_neighbors)
