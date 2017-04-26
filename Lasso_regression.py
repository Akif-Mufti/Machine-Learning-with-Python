# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 16:02:08 2017

@author: user
"""
#Ridge Regression 
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import mglearn
try:
    from sklearn.datasets import train_test_split
except ImportError:
    from sklearn.cross_validation import train_test_split
x,y= mglearn.datasets.load_extended_boston()
x_train,x_test,y_train,y_test = train_test_split(x,y,random_state = 0)
lr=LinearRegression().fit(x_train,y_train)
print("lr.coef_: %s" % lr.coef_)
print("lr.intercept_: %s" % lr.intercept_)
print("training set score: %f" % lr.score(x_train, y_train))
print("test set score: %f" % lr.score(x_test, y_test))

#In this case we will witness very different  test and training score, it is overfitting .

ridge=Ridge().fit(x_train,y_train)
print("train set score : %f"% ridge.score(x_test,y_test))

#Difference here is small when compared to the results obtained in ordinary least square it is overfitting.
#Here we are less likely to overfit
print("training set score : %f" % ridge.score(x_train,y_train))

##Now changing the value of alpha
ridge10=Ridge(alpha=10).fit(x_train,y_train)
print("training set score : %f" % ridge10.score(x_train,y_train))
print("train set score : %f"% ridge10.score(x_test,y_test))

#Higher value of alpha means a more restricted model
ridge01=Ridge(alpha=0.1).fit(x_train,y_train)
print("training set score : %f" % ridge01.score(x_train,y_train))
print("train set score : %f"% ridge01.score(x_test,y_test))
#lower alpha improves the generalization
plt.title("ridge_coefficients")
plt.plot(ridge.coef_,'o',label="Ridge alpha =1")
plt.plot(ridge10.coef_,'o',label="Ridge alpha =10")
plt.plot(ridge01.coef_,'o',label="Ridge alpha =0.1")
plt.plot(lr.coef_,'o',label="Linear Regression")
plt.ylim(-25,25)
plt.legend()
#lasso does very bad with both training and testing, 
lasso = Lasso().fit(x_train,y_train)
print("training set score :%f"%lasso.score(x_train,y_train))
print("testing set score :%f"%lasso.score(x_test,y_test))
print("number of features :%d"%np.sum(lasso.coef_!=0))
# decreaing the value of alpha , it works better for training and testing
lasso001 = Lasso(alpha=0.01).fit(x_train,y_train)
print("training set score :%f"%lasso001.score(x_train,y_train))
print("testing set score :%f"%lasso001.score(x_test,y_test))
print("number of features :%d"%np.sum(lasso001.coef_!=0))
#If we set alpha too low, we again remove the effect of regularization and end up with a result similar to LinearRegression.
lasso0001 = Lasso(alpha=0.001).fit(x_train,y_train)
print("training set score :%f"%lasso0001.score(x_train,y_train))
print("testing set score :%f"%lasso0001.score(x_test,y_test))
print("number of features :%d"%np.sum(lasso0001.coef_!=0))

plt.plot(lasso.coef_,'o',label="Ridge alpha =1")
plt.plot(lasso001.coef_,'o',label="Ridge alpha =0.01")
plt.plot(lasso0001.coef_,'o',label="Ridge alpha =0.001")
plt.plot(ridge01.coef_,'o',label="Ridge alpha =0.1")
plt.plot(lr.coef_,'o',label="Linear Regression")
plt.ylim(-25,25)
plt.legend()



