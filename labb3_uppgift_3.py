# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 18:09:17 2022

@author: david
"""

import random
while True:
    kast_spelare = []
    min = 1
    max = 6
    antal_kast = int(input("Hur många kast?\n"))
    antal_tärn = int(input("Hur många tärningar vill du kasta?\n"))
    börja_kasta = input("Genom att trycka på enter kan du börja kasta, om du vill avsluta spelet skriv A:\n")
    if börja_kasta == "A":
        print("Fuck you")
    else:
        i = 0
        j = 0
        while i < antal_tärn:
            kast_spelare.append(random.randint(min, max))
            i += 1
            #Skapar en lista med resultat från respektive tärning
            #Listans kardinarlitet är antalet tärningar
        for j in range(len(kast_spelare)):
            #print("kast_spelare: %d" %(kast_spelare[j]))
            print("Tärning", str(j+1),": " ,kast_spelare[j])
    while antal_kast > 1:
        kasta_igen = input("Vill du kasta igen? (j/n)\n")
        if kasta_igen != "j":
            print("Skit i det då")
            break
        else:
            a = 0
            kast_spelare.clear()
            #Elementen i kast_spelare läggs till i alla_kast_spelare
            #Kast_spelare töms sedan för att göra plats för nya element
            while a < antal_tärn:
                kast_spelare.append(random.randint(min, max))
                a += 1
            for i in range(len(kast_spelare)):
                print("Tärning", str(i+1), ": ", kast_spelare[i])
        #if a == antal_tärn - 1:
         #   print("Du fick ", *kast_spelare)
            #print("Du fick ", kast_spelare[i])
        antal_kast = antal_kast - 1
    print("Du fick ", *kast_spelare)
    while True:
        svar = str(input("Är ny spelare redo att kasta? (j/n):\n"))
        if svar in ('j', 'n'):
            break
        print("invalid input.")
    if svar == 'j':
        continue
    else:
        print("Skit i det då")
        break