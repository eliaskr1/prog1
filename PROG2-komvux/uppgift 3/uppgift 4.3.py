# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 20:57:35 2023

@author: elias
"""

#uppgift 4.3

import os

def dir_list(): # funktion som skapar en lista med filer i aktuell katalog
    global f_list
    f_list = []
    for item in os.listdir(): # loopar igenom os.listdir (aktuell katalog)
        if os.path.isfile(item): # kollar om varje item är en fil eller inte
            f_list.append(item) # lägger till filer i listan
        else:
            continue # skippar andra objekt
        
dir_list()

for l in f_list: # listar ut listan
    print(l)