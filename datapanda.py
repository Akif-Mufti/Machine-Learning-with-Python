# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 15:11:56 2017

@author: user
"""

# Load CSV using Pandas
from pandas import read_csv
from pandas import set_option
filename = 'pima-indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
print(data.shape)
# View first 20 rows
peek = data.head(20)
print(peek)

types = data.dtypes
print(types)
data = read_csv(filename, names=names)
set_option('display.width', 100)
set_option('precision', 3)
# Statistical Summary
description = data.describe()
print(description)
# Class Distribution
class_counts = data.groupby('class').size()
print(class_counts)
# Pairwise Pearson correlations
correlations = data.corr(method='pearson')
print(correlations)
# Skew for each attribute
skew = data.skew()
print(skew)