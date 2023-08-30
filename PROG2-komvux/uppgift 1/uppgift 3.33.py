# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 20:21:15 2023

@author: elias
"""

# Uppgift 3.33

from random import randint

l = [randint(-100, 101) for i in range(100)] #generera lista, taget från boken

x = 0

def negToZero(x):
    for i in l: # Loopar igenom listan
        if i < 0: # om i är mindre än 0 (negativt)
            l[x] = 0 # omvandlas talet till 0
            x += 1
        else: # annars fortsätter loopen 
            x += 1

negToZero(x) # callar funktionen
    
print(l)