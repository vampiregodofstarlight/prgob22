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
        j = i.strip()
        tvlist.append(j.split(','))
        for a in range(len(tvlist)):
            for b in range(1,len(tvlist[a])):
                tvlist[a][b]=int(tvlist[a][b])
                #print(type(tvlist[a][b]))
                #print((tvlist[a][b]))
    #TVlist=sum(tvlist,[])
    tvfile.close()
    #print(tvlist[0])
    tv=TV(tvlist[0])
    return(tvlist)
        
print(read_file('tvfil.txt'))


def write_file(tvlist, tv_file):
    tvfile = open(tv_file, 'w')
    for i in range(len(tvlist)):
        tvfile.write(i)
    tvfile.close()
    
    
    
tvlist = read_file("tvfil.txt")  
#for tv in tvlist: print(tv)

#tvlist[0].change_channel(1)
#for tv in tvlist: print(tv)
