# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 14:23:46 2017

@author: user
"""
from collections import Counter
from matplotlib import pyplot as plt

mentions = [500,505]
years = [2013,2014]
plt.bar([2012.6,2013.6],mentions,0.8)
plt.xticks(years)
plt.ylabel("Number of times i heard someone say Data Science")
# if you don't do this, matplotlib will label the x-axis 0, 1
# and then add a +2.013e3 off in the corner (bad matplotlib!)
#plt.ticklabel_format(useOffset = False)
#plt.axis([2012.5,2014.5,499,506])
#plt.title("Look at the 'Huge' Increase!")
#plt.show()
plt.axis([2012.5,2014.5,0,550])
plt.title("Look at the 'Huge' Increase!")
plt.show()