# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 16:27:06 2023

@author: elias
"""

#uppgift 3.36

l =  [
     [45, 78, 56, 34], 
     [9, 23, 23], 
     [34, 87], 
     [12, 19, 78, 56, 45]
     ]

with open("myfile.txt", "w") as file:
    for x in range(len(l)): #.join() funktionen används så att värden i listan separeras av " " och så att listan 
                            #inte skrivs in med brackets och kommatecken.
        file.write(" ".join(map(str, l[x]))) #konverterar också raderna i min lista till strings så att de kan skrivas in i filen
        file.write(" \n") #efter varje rad skrivs in behvös radbrytstecknet för att skriva på olika rader.