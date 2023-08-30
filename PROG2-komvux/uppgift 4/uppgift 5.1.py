# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 17:17:55 2023

@author: elias
"""

# uppgift 5.1
import numpy as np

# skapar en array med värden mellan 1-4 (1, 2, 3)
a = np.array(np.arange(1, 4)) 

# skapar en array mellan 1-8. här måste jag specifiera dtype annars blir det
# en heltals array då step = 1
b = np.array(np.arange(1, 8, 1, float))

print(a)

print(b)