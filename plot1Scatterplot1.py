# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 14:23:46 2017

@author: user
"""
from collections import Counter
from matplotlib import pyplot as plt

variance= [1,2,4,8,16,32,64,128,256]
bias =[256,128,64,32,16,8,4,2,1]
label = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
plt.scatter(variance,bias)

for lab,bi,var in zip(label,bias,variance):
    plt.annotate(lab , 
                 xy =(var,bi) , 
                xytext=(5,-5) ,
                textcoords='offset points')
plt.title("variance Vs Bias")
plt.xlabel("Variance")
plt.ylabel("Bias")
plt.show()
