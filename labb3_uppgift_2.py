# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 18:09:23 2022

@author: david
"""
#print("{:nd}".format(x)) printar x med mellanrum n 
rad = int(input("Ange antal rader:\n"))
kol = int(input("Ange antal kolumner:\n"))
i = 0
while i <= rad:
    j = 0
    while j <= kol:
        if i + j == 0:
            print("{:4s}".format(""),end="")
            #i+j=0 => i,j=0
            #här printas ett tomt mellanrum med storleken 4
            #s då vi vill formatera ""(en sträng)
        elif i * j == 0 :
            print("{:4d}".format(i+j),end="") #gräns
            #i*j=0 => i=0 eller j=0
            #här printas gränserna till tabellen med samma avstånd 4
            #i och j växer till vad användaren angivit som input på rad/kol
            #d då vi vill formatera siffror(digits)
        else :
            print("{:4d}".format(i*j),end="")
            #när i*j!=0 skapas själva tabellen
            #tabellen växer efter varje iteration baserat på användares input
        j = j + 1   
    print()
    i = i + 1