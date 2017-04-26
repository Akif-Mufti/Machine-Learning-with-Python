# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 14:23:46 2017

@author: user
"""
from collections import Counter
from matplotlib import pyplot as plt

variance= [1,2,4,8,16,32,64,128,256]
bias =[256,128,64,32,16,8,4,2,1]
totalError = [x+y for x,y in zip(variance,bias)]
y = zip(bias, variance)

xs=[i for i,_ in enumerate(variance)]
#Showing multiple series on same chart
plt.plot(xs, variance, 'g-', label='variance') # green solid line
plt.plot(xs, bias, 'r-', label='bias') # green solid line
plt.plot(xs, totalError, 'o:', label='TotalError') # blue 
plt.legend(loc=9)
plt.xlabel("Model Complexity")
plt.title("bias Variance tradeoff")
plt.show()
