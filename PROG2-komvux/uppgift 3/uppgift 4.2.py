# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 19:20:54 2023

@author: elias
"""

# uppgift 4.2

import os
   
u_input = "PATH" # fyll i miljövariabel

if u_input in os.environ: # om input variabeln finns i os.environ printas det att den finns
    print(u_input + " är med i os.environ")
else: # annars printas det att den inte finns
    print(u_input + " är inte med i os.environ")