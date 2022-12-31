# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 00:09:18 2022

@author: david
"""

class Cinema:
    def __init__(self, cinema_name, total_seats, pen_ticket_price, adu_ticket_price, chi_ticket_price, sold_pen_tickets, sold_adu_tickets, sold_chi_tickets, reservations):
        self.cinema_name = cinema_name
        self.total_seats = total_seats
        self.pen_ticket_price = pen_ticket_price
        self.adu_ticket_price = adu_ticket_price
        self.chi_ticket_price = chi_ticket_price
        self.sold_pen_tickets = sold_pen_tickets
        self.sold_adu_tickets = sold_adu_tickets
        self.sold_chi_tickets = sold_chi_tickets
        self.reservations = reservations
        
    def __str__(self):
        return f'{self.cinema_name},{self.total_seats},{self.pen_ticket_price},{self.adu_ticket_price},{self.chi_ticket_price},{self.sold_pen_tickets},{self.sold_adu_tickets},{self.sold_chi_tickets}'
    
def intro():
    print('Welcome!\nThis program tracks revenue and reservations for cinemas in Stockholm.')
    
def revenue(cin_obj):
    revenue_list = []
    for i in range(len(cin_obj)):
        revenue_pen = int(cin_obj[i].pen_ticket_price) * int(cin_obj[i].sold_pen_tickets)
        revenue_adu = int(cin_obj[i].adu_ticket_price) * int(cin_obj[i].sold_adu_tickets)
        revenue_chi = int(cin_obj[i].chi_ticket_price) * int(cin_obj[i].sold_chi_tickets)
        
        revenue_sum = revenue_pen + revenue_adu + revenue_chi
        revenue_list.append(revenue_sum)
    return revenue_list

def revenue_sum(revenue_list):
    total_revenue = sum(revenue_list)
    print(f'Total revenue for all cinemas was {total_revenue}kr.')
    

def read_cinema_file():
    file_input = str(input('Choose existing cinema file: '))
    cin_list = []
    #Empty list to store file info
    try:
        cin_file = open(file_input+'.txt', 'r', encoding="utf-8")
        for line in cin_file:
            lines = line.rstrip()
            cin_list.append(lines)
    #Opens the file(specified by user input) and iterates over each line in file
    #Each line is split into multiple elements which are then appended to cin_list
        return cin_list
    except FileNotFoundError:
        print('File does not exist, try again!')
        return read_cinema_file()
    #If the file does not  exist in this folder, a FileNotFoundError is raised and caught
    #giving the user another attempt

def cinema_reservations(cin_list):
    for i in range(len(cin_list)):
        print(f'{cin_list[i].cinema_name}, {cin_list[i].reservations}%')

def read_int(sstr):
    try:
        return int(input(sstr))
    except ValueError:
        print("Input must be an integer, try again!")
        return read_int(sstr)

    
def create_cinema_obj(cin_list): #FELKONTROLL
    cin_obj_list = []
    for i in range(len(cin_list)):
        cin_split = cin_list[i].split(',')
        amount_sold_pen = read_int((f'How many pensioner tickets were sold by {cin_split[0]}?'))
        amount_sold_adu = read_int((f'How many adult tickets were sold by {cin_split[0]}?'))
        amount_sold_chi = read_int((f'How many child tickets were sold by {cin_split[0]}?'))

        reservations = round((amount_sold_pen + amount_sold_adu + amount_sold_chi)*100/int(cin_split[1]), 2)
        cin_obj = Cinema(cin_split[0], cin_split[1], cin_split[2], cin_split[3], cin_split[4], amount_sold_pen, amount_sold_adu, amount_sold_chi, reservations)
        cin_obj_list.append(cin_obj)
        return cin_obj_list
    
def main():
    intro()
    read_Cfile = read_cinema_file()
    C_obj = create_cinema_obj(read_Cfile)
    print('A list of the revenue of each cinema\n')
    cin_rev = revenue(C_obj)
    revenue_sum(cin_rev)
    print('Here are the reservations for each cinema:\n')
    cinema_reservations(C_obj)
    print('Here is a sorted list of the reservations:\n')
    sorted_list = sorted(C_obj, key=lambda Cinema:Cinema.reservations)
    sorted_list.reverse()
    for i in sorted_list:
        print(f'{i.cinema_name}, {i.reservations}%')
        
main()
