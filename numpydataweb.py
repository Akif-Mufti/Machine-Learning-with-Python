# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 15:08:28 2017

@author: user
"""

# Load CSV from URL using NumPy
from numpy import loadtxt
from urllib import urlopen
url = 'https://goo.gl/vhm1eU'
raw_data = urlopen(url)
dataset = loadtxt(raw_data, delimiter=",")
print(dataset.shape)