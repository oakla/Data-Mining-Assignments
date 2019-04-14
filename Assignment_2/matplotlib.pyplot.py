# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 10:27:26 2018

@author: oakl
"""
#matplotliib expects data to be np.array or np.ma.masked_array
import matplotlib.pyplot as plt
import numpy as np
import pandas

fig = plt.figure()  # an empty figure with no axes
fig.suptitle('No axes on this figure')  # Add a title so we know which it is

fig, ax_lst = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes


a = pandas.DataFrame(np.random.rand(4,5), columns = list('abcde'))
a_asndarray = a.values

print(a)

plt.show()

x = np.linspace(0, 2, 100)

plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')

plt.xlabel('x label')
plt.ylabel('y label')

plt.title("Simple Plot")

plt.legend()

plt.show()