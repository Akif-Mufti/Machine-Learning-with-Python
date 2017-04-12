# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 12:47:27 2017

@author: user
"""

#Matplotlib
import matplotlib.pyplot as plt
import numpy
myarray = numpy.array([1, 2, 3,4,9,10,19])
plt.plot(myarray)
plt.xlabel('some x axis')
plt.ylabel('some y axis')
plt.show()
x = numpy.array([1, 2, 3])
y = numpy.array([2, 4, 6])
plt.scatter(x,y)
plt.xlabel('some x axis')
plt.ylabel('some y axis')
plt.show()