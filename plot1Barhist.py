# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 14:23:46 2017

@author: user
"""
from collections import Counter
from matplotlib import pyplot as plt

grades = [83,95,67,54,23]
decile = lambda grade:grade // 10*10
histogram = Counter(decile(grade) for grade in grades)
plt.bar([x-4 for x in histogram.keys()], histogram.values(),8)
plt.axis([-5,105,0,5]) 
plt.xticks([10*i for i in range(11)])
plt.xlabel("Decline")
plt.ylabel("# of students")
plt.title("Distribution of Exam one grade")
plt.show()

