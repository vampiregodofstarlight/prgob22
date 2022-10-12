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
    

def change_channel(tv_obj):
    try:
        channel = int(input("Choose channel:\n"))
        tv_obj.change_channel(channel)
    except ValueError:
        print('Invalid input')
        return(change_channel(tv_obj))

def increase_volume(tv_obj):
    tv_obj.increase_volume()
        
def decrease_volume(tv_obj):
    tv_obj.decrease_volume()
    
def adjust_TV_menu():
    try:
        options=list(range(1,5))
        for i in options:
            if i == 1:
                print(str(i)+'.','Change channel','\n')
            elif i == 2:
                print(str(i)+'.','Increase volume','\n')
            elif i == 3:
                print(str(i)+'.','Decrease volume','\n')
            elif i == 4:
                print(str(i)+'.','Return to main menu','\n')
            
        choose_input = int(input('Choose alternative: '))
        for i in range(len(options)):
            if choose_input == options[i]:
                return_input = choose_input
        return(return_input)
    except Exception:
        print('Invalid input, try again!')
        return(adjust_TV_menu())
        
def select_TV_menu(tv_list):
    
    
    
tvlist = read_file("tvfil.txt")  
#for tv in tvlist: print(tv)

#tvlist[0].change_channel(1)
#for tv in tvlist: print(tv)
