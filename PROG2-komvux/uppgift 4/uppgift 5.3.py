# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 16:50:37 2023

@author: elias
"""

# Uppgift 5.3

import numpy as np
# funktion tagen från boken för att få fram minnesallokering
def memory_of(b):
    return b.__array_interface__["data"][0]

b = np.array([[1, 2, 3], [4, 5, 6]], float)

print (b)
print("array shape =", b.shape) # Storlek
print("array ndim =", b.ndim) # n-dimensioner
print("array dtype =", b.dtype) # Datatyp
print("array size =", b.size) # Antal element
print("array itemsize =", b.itemsize) # Storlek i byte
print("array memory allocation =", memory_of(b)) # Minnesallokering
print("array memory area =", b.data) # Minnesområde

#det här var det jag kunde hitta i kapitlet som stämde överens med uppgiften