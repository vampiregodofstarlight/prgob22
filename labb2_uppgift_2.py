# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 16:07:26 2022

@author: david
"""

#UPPGIFT 2
p_vikt = float(input("Ange paketets vikt i kg:\n"))
#Input ber användaren om ett flyttal
if 0 < p_vikt <= 2:
    pris = 30*p_vikt
elif 2 <= p_vikt < 6:
    pris = 28*p_vikt
elif 6 <= p_vikt < 12:
    pris = 25*p_vikt
elif p_vikt >= 12:
    pris = 23*p_vikt
else:
    raise ValueError("Ogiltig vikt, pris kan ej beräknas")
       
#Matar användaren in ett ogiltigt värde(<0) avslutas programmet :)
#Användaren bör veta bättre!
print("Ditt paket kostar ",round(pris, 1) ,"kr att skicka.")
#Uppfyller flyttalet någon av ovanstående olikheter
#beräknas det tillhörande kilopriset, enligt given formel, som sedan printas