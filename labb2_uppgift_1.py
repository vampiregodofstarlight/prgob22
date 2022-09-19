# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 16:07:26 2022

@author: david
"""

#UPPGIFT 1
sträcka = float(input("Ange körsträcka i km:\n"))
#När programmet körs, frågas användaren hur många kilometer bilen har kört
#Användaren ger en input i form av ett flyttal för att svara på frågan
#Inputten sparas i variabeln "sträcka", för att användas i uträkning senare                                           
print("Ange antal liter brukat bränsle:\n") 
liter = float(input())
#Samma princip här, flyttalet sparas här i variabeln "liter"
bf = ((liter/sträcka)*100)
#bränsleförbrukningen räknas nu med respektive input
print("Liter/100km")
print(round(bf, 3))
#Slutligen printas rubriken "Liter/100km" tillsammans med
#den avrundade bränsleförbrukningen

