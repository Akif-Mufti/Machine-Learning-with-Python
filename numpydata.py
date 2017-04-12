# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 15:07:38 2017

@author: user
"""
#You can load your CSV data using NumPy and the numpy.loadtxt() function. This function
#assumes no header row and all data has the same format. The example below assumes that the
#
le pima-indians-diabetes.data.csv is in your current working directory.
# Load CSV using NumPy
from numpy import loadtxt
filename = 'pima-indians-diabetes.data.csv'
raw_data = open(filename, 'rb')
data = loadtxt(raw_data, delimiter=",")
print(data.shape)