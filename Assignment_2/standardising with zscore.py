# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 15:00:34 2018

@author: oakl
"""

##Answer to question 2.1.1a
import scipy.stats

a = [1, 3.4 ,-1, 5, 10, 44, -2] #these values span axis=0, ie this is column vector

x = scipy.stats.zscore(a)

print(a, "\nx becomes\n", x )

x0 = scipy.stats.zscore(a,axis=0)
print(a, "\nx0 becomes\n", x0)

b = [[1, 3.4 ,-1, 5, 10, 44, -2], #to standardize each row, set axis=1
     [5, 5.5, 0, 8, 9, 12, 11]]

y = scipy.stats.zscore(b, axis=0)

print(b, "\nbecomes\n", y )

