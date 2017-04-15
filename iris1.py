# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 15:13:29 2017

@author: user
"""
import matplotlib.pyplot as plt
import numpy as np 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
try:
    from sklearn.datasets import train_test_split
except ImportError:
    from sklearn.cross_validation import train_test_split

iris = load_iris()
iris.keys()
print(iris['DESCR'][:193] + "\n...")
#dict_keys(['data', 'target', 'target_names', 'DESCR', 'feature_names'])
#Remember that the individual items are called samples in machine learning, and their properties are called features.
#iris['data'].shape
iris['data'][:5] #first five samples

type(iris['data'])

x_train,x_test,y_train,y_test = train_test_split(iris['data'],iris['target'],random_state = 0)
fig, ax = plt.subplots(3, 3, figsize=(30, 30))
plt.suptitle("iris_pairplot")
for i in range(3):
    for j in range(3):
        ax[i, j].scatter(x_train[:, j], x_train[:, i + 1], c=y_train, s=60)
        ax[i, j].set_xticks(())
        ax[i, j].set_yticks(())
        if i == 2:
            ax[i, j].set_xlabel(iris['feature_names'][j])
            if j == 0:
                ax[i, j].set_ylabel(iris['feature_names'][i + 1])
                if j > i:
                    ax[i, j].set_visible(False)
                    
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(x_train, y_train)
KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
metric_params=None, n_jobs=1, n_neighbors=1, p=2,
weights='uniform')
#testing X_new = np.array([[5, 2.9, 1, 0.2]]) // iris['target_names'][prediction]
#evaluation the model
y_pred = knn.predict(x_test)
l=np.mean(y_pred == y_test)

ac= knn.score(x_test, y_test)
