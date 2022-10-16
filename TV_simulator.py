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
    for c in range(len(tvlist)):
        tv_obj=TV(tvlist[c][0],tvlist[c][1],tvlist[c][2],tvlist[c][3],tvlist[c][4])
        objlist.append(tv_obj)
    tvfile.close()
    #print(tvlist)
    return(objlist)
        
#print(read_file('allatv.txt'))


def write_file(tvlist, tv_file):
    tvfile = open(tv_file, 'w')
    for i in range(len(tvlist)):
        tvfile.write(tvlist[i].str_for_file()+'\n')
    tvfile.close()
 
    
def channel_input(tv_obj):
    channel = int(input('Choose channel: '))
    if channel < 1:
        raise Exception('Channel cant be negative')
    if channel > tv_obj.max_channel:
        raise Exception('Max channel is ', tv_obj.max_channel)
    return(channel)
#"channel_input" raises exceptions for when user input is not within correct range           

def change_channel(tv_obj):
    try:
        tv_obj.change_channel(channel_input(tv_obj))
        #returns "channel_input"(integer)
    except Exception:
        print( f'Channel must be in range 1-{tv_obj.max_channel}, try again!')
        return(change_channel(tv_obj))
    #Exceptions raised in "channel_input" are caught here

def increase_volume(tv_obj):
    tv_obj.increase_volume()
        
def decrease_volume(tv_obj):
    tv_obj.decrease_volume()
#"increase_volume" and "decrease_volume" simply calls on the required methods    
    
def choose_adjust_options():
    adjust_input = int(input('Choose alternative: '))
    if adjust_input < 1:
      raise ValueError("lower than 1")
    if adjust_input > 4:
      raise ValueError("higher than 4")
    return adjust_input
#Exceptions for incorrect inputs used in "adjust_TV_menu" are raised here

def adjust_TV_menu():
  options = list(range(1,5))
  for i in options:
    if i == 1:
      print(str(i)+'.','Change channel')
    elif i == 2:
      print(str(i)+'.','Increase volume')
    elif i == 3:
      print(str(i)+'.','Decrease volume')
    elif i == 4:
      print(str(i)+'.','Return to main menu')
#For every value of i in the given range,
#a row with a descripitve string is printed
  
  try:
    return choose_adjust_options()
    #"choose_adjust_options" is called and returns an integer
  except:
    print('Invalid input, try again!')
    return adjust_TV_menu()
#The exceptions raised in "choose_options" are caught here

TV_list = read_file('allatv.txt')

def choose_menu_options():
    menu_input = int(input('Choose a TV or exit the program: '))
    if menu_input < 1:
        raise Exception('Lower than 1')
    return menu_input
#Exception for when user input < 1

def select_TV_menu(tv_list):
    for i in range(len(tv_list)):
        print(str(i+1)+'.',tv_list[i].tv_name)
        #Iterates over tv_list and prints object name using "tv_name" method
    print(str(len(tv_list)+1)+'.', 'Exit program')
    #Prints the last line "Exit program" with appropriate number -> list lenght + 1
    try:
        menu_input = choose_menu_options()
        if menu_input == len(tv_list)+1:
            return(None)
        else:
            return(tv_list[(menu_input-1)])
    except Exception:
        print('Invalid input, try again!')
        return select_TV_menu(TV_list)
#"Exception" handles any IndexErrors + any exceptions raised in "choose_menu_options"
    
def main():
    print('Welcome to the TV simulator!\n')
    while True:
        TV_list = read_file('allatv.txt')
        selected_TV = select_TV_menu(TV_list)
        if selected_TV == None:
            print('Thank you for using my TV simulator :3')
            #write_file(TV_list, 'allatv.txt')
            break
        #if select_TV_menu() returns None, the while True loop breaks and
        #the program quits
        while True:
            print('\n')
            print(str(selected_TV))
            adjust_variable = adjust_TV_menu()
            if adjust_variable == 1:
                change_channel(selected_TV)
            elif adjust_variable == 2:
                increase_volume(selected_TV)
            elif adjust_variable == 3:
                decrease_volume(selected_TV)
            elif adjust_variable == 4:
                break
            write_file(TV_list, 'allatv.txt')
            #after each iteration, the textfile is cleared and
            #the updated TV_list is added to the textfile 
main()
