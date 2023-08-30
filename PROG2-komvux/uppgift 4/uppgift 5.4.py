# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 16:59:10 2023

@author: elias
"""

# uppgift 5.4

import numpy as np

a = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]) #array tagen från boken

a_long = np.reshape(a, [12]) # ändrar arrayen till 1 dimension

print (a_long)

print (a_long.ndim) # skriver ut hur många dimensioner a_long är