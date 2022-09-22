# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 20:31:21 2022

@author: david
"""

def chomp(M, r, c):
    for i in range(r, len(M)):
        #
        for j in range(c, len(M[i])):
            #
            del M[i][c:]
    return(M)
    
