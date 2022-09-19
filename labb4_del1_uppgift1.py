# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 14:24:18 2022

@author: david
"""

def create_chocolate_bar(x,y):
    matris = []
    #En tom lista för att appenda rader till
    for i in range(int(x)):
        rad = []
        #Värdet på x kommer ange antalet rader
        #Varje iteration skapar en ny rad
        #Kardinaliteten av respektive rad är ekvivalent matrisens antal kolumner
        for j in range(int(y)):
            rad.append(str(i+1)+str(j+1))
        matris.append(rad)
    return matris
        