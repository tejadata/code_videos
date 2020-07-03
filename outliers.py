# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 18:37:33 2020

@author: vishwateja.r
"""


import numpy as np
import matplotlib.pyplot as plt 

values= [1,2,3,12,32,64,99,121,-223,123,43,90,200,350]



values = np.array(values)

q1 = np.quantile(values,0.25)
q2 = np.quantile(values,0.50)
q3 = np.quantile(values,0.75)

iqr = q3-q1

higer = q3 + (1.5*iqr)
lower = q1 - (1.5*iqr)

plt.boxplot(values)
