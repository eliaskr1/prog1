# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 17:15:04 2023

@author: elias
"""

# Övning 6.3

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.0, 2*np.pi, 1000)
y = np.sin(x)

plt.plot(x, y)