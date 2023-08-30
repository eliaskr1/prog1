# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 20:26:58 2023

@author: elias
"""
# Uppgift 3.32

import math
  
# funktion för att kolla om tal "n" är ett primtal
def check(n):
    if n == 1: # 1 är inte ett primtal men hade returnat true
        return False
    for x in range(2, (int)(math.sqrt(n))+1): # metod tagen från boken
        if n % x == 0:
            return False 
    return True

# loop som kör check() funktionen på varje heltal mellan 2-100.
for x in range(2, 100):
    if check(x): # om check() returnar true så printas primtalet och loopen fortsätter
        print(x)
        x += 1
    else: # om false så fortsätter endast loopen
        x += 1