# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 14:57:34 2017

@author: user
"""
import numpy as np
from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
cancer.keys()
print(cancer.data.shape)
print(cancer.target_names)
np.bincount(cancer.target)
cancer.feature_names
