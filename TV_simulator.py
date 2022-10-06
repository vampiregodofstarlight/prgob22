# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 17:36:01 2022

@author: david
"""

from TV import TV

def read_file(tv_file):
    tvfile = open(tv_file, 'r')
    tvlist = []
    objlist = []
    for i in tvfile:
        j = i.strip()
        tvlist.append(j.split(','))
        for a in range(len(tvlist)):
            for b in range(1,len(tvlist[a])):
                tvlist[a][b]=int(tvlist[a][b])
                #tv_obj=TV()
    #print(tv_obj)
    for c in range(len(tvlist)):
        tv_obj=TV(tvlist[c][0],tvlist[c][1],tvlist[c][2],tvlist[c][3],tvlist[c][4])
        objlist.append(tv_obj)
    tvfile.close()
    return(objlist)
        
print(read_file('allatv.txt'))


def write_file(tvlist, tv_file):
    tvfile = open(tv_file, 'w')
    for i in range(len(tvlist)):
        tvfile.write(tvlist[i].str_for_file()+'\n')
    tvfile.close()
    

tvlista = read_file("allatv.txt")
tvlista[0].change_channel(1)
tvlista[0].decrease_volume()   
write_file(tvlista, "allatv.txt")    
for tv in tvlista: print(tv) 
    
    
    
tvlist = read_file("tvfil.txt")  
#for tv in tvlist: print(tv)

#tvlist[0].change_channel(1)
#for tv in tvlist: print(tv)
