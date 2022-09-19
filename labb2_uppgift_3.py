# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 16:07:27 2022

@author: david
"""
#UPPGIFT 3
summa_pris = 0
paket = []
i = 0
j = 0
antal = int(input("Hur många paket vill du skicka?\n"))
while i < antal:
    vikt = float(input("Vad är vikten på paketet " + str(i+1) + "?\n"))
    paket.append(int(vikt))
    i += 1
while j < len(paket):
    if 0 < int(paket[j]) <= 2:
        pris = 30*paket[j]
    elif 2 <= int(paket[j]) < 6:
        pris = 28*paket[j]
    elif 6 <= int(paket[j]) < 12:
        pris = 25*int(paket[j])
    elif int(paket[j]) >= 12:
        pris = 23*int(paket[j])
    else:
        raise ValueError("Ogiltig vikt, pris kan ej beräknas")
    summa_pris = summa_pris + pris
    pris = 0
    j += 1
print("Det kostar " + str(summa_pris) + "kr att skicka dessa paket")