# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 12:29:00 2018

@author: oakl
"""
##Answer to question 2.1.1a
import scipy.io
import matplotlib.pyplot as plt
import numpy as np

wine_mat = scipy.io.loadmat('./Data/wine.mat')

print(wine_mat)

for k, v in wine_mat.items():
    print('The key *', k,'* has the value *', v, '*\n***')

print(wine_mat['attributeNames'])