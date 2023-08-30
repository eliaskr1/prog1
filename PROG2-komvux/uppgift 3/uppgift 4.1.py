# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 18:36:25 2023

@author: elias
"""

# uppgift 4.1

import os

def l_path():
    exe_l = os.environ["PATH"] # skapar en variabel med alla sökvägar i "PATH"
    l = exe_l.split(";") # eftersom jag är på windows delas dessa till en lista med ";"
    for path in l: # loopar igenom listan
        print(path) # printar varje sökväg i listan
    
l_path()


