# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 15:11:56 2017

@author: user
"""

# Univariate Histograms
from matplotlib import pyplot
from pandas import read_csv
filename = 'pima-indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
data.hist()
pyplot.show()
# Univariate Density Plots
data = read_csv(filename, names=names)
data.plot(kind='density', subplots=True, layout=(3,3), sharex=False)
pyplot.show()
# Box and Whisker Plots

data.plot(kind='box', subplots=True, layout=(3,3), sharex=False, sharey=False)
pyplot.show()