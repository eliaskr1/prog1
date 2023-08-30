# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 17:31:06 2023

@author: elias
"""

# Uppgift 5.7

import numpy as np

a = np.ones([10, 10], int)  #ones funktionen skapar en flyttals-array av ettor
                            #här behöver jag specifiera dtype och shape
print(a)

print(a.dtype)