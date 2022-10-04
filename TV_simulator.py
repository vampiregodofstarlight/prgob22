# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 17:36:01 2022

@author: david
"""

from TV import TV

def read_file(tv_file):
    tvfile = open(tv_file, 'r')
    tvlist = []
    for i in tvfile:
        tvlist.append(i)
    return(tvlist)
        
print(read_file('allatv.txt'))
