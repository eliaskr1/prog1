# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 17:48:53 2023

@author: elias
"""

#uppgift 3.37

with open("myfile.txt", "r") as file:
    
        strings = file.read() #läser in textfilen till en lång sträng
        l = strings.split(" ") #separerar strängen till en lista. bryten i listan specifieras i split(" ")
        newL = [s.strip("\n") for s in l] #skapar en ny lista utan radbrytstecken
        newL.remove("") #tar bort ett tomt list index som blev skapat av koden i uppgift 3.36
        
        newL = [int(i) for i in newL] #konverterar resterande list värden till heltal
        
        print (newL)