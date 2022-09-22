# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 15:22:10 2022

@author: david
"""
#UPPGIFT 2
def print_chocolate_bar(M):
    for i in range(len(M)):
        print("\n")
        #After every row, a new line is printed
        for j in range(len(M[i])):
            print("{:3s}".format(M[i][j]), end="")
            #Along each list, every element M[i][j] is
            #printed, with a minimum width of 3, aligned to the right
    return None
#Iterera över och printa en liten lista i taget?

        
            
    
    
        
