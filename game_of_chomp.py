# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 22:37:14 2022

@author: david
"""

def create_chocolate_bar(x,y):
    M = []
    #An empty list for appending rows to
    for i in range(int(x)):
        row = []
        #The value of x will determine the amount of rows
        #Every iteration creates a new row
        #The cardinality of each row is equivalent to the amount of columns
        for j in range(int(y)):
            row.append(str(i+1)+str(j+1))
            #Each element is appended to row
        M.append(row)
        #Row is now appended to matrix
        M[0][0] = "P"
    if x <= 0 or y <=0:
        return None
    else:
        return M
    

def print_chocolate_bar(M):
    for i in range(len(M)):
        print("\n")
        #After every row, a new line is printed
        for j in range(len(M[i])):
            print("{:3s}".format(M[i][j]), end='')
            #Along each list, every element M[i][j] is
            #printed, with a minimum width of 3, aligned to the right
    return None


def chomp(M, r, c):
    for i in range(r-1, len(M)):
        for j in range(c-1, len(M[i])+1):
            del M[i][c-1:]
    while [] in M:
        M.remove([])
    return(M)


def check_winner(M):
    for i in range(len(M)):
        if len(M)==1 and len(M[i])==1:
            return True
        else:
            return False
        
        
def ask_cell_number(M):
        cell_number = input("Välj en ruta: \n")
        for i in range(len(M)):
            for j in range(len(M[i])):
                if cell_number==M[i][j]:
                    returnValue = (i+1, j+1)
                elif cell_number == "P":
                    print('Spelaren får ej välja den giftiga rutan')
                    return ask_cell_number(M)
        try:
            return returnValue
        except UnboundLocalError:
            print("Ruta", cell_number, "finns ej i spelplanen, försök igen!\n")
            return ask_cell_number(M)
        
        
#GAME OF CHOMP

def main():
    print('Välkommen till spelet Chomp.\nInstruktioner: I spelet kommer du utmanas om att välja ett blocknummer från spelplanen. Det valda blocket och alla block under och till högre kommer att raderas. Spelet går ut på att undvika välja P, den spelare som väljer P förlorar och den andra spelare vinner.')

    row_board = int(input('Hur många rader önskas?\n'))
    col_board = int(input('Hur många kolumner önskas?\n'))

    M=create_chocolate_bar(row_board, col_board)
    print_chocolate_bar(M)
    print('\n')
    max_spelare = 2

    spelare = 0

    while check_winner(M) == False:
        while True:
            print("spelare {} turn".format(spelare+1))
            #input("enter for next {}".format("player" if player + 1 < max_players else "round"))
            spelare = (spelare + 1) % max_spelare
            r,c=ask_cell_number(M)
            chomp(M,r,c)
            print_chocolate_bar(M)
            #print('\n',M)
            print('\n')
            if check_winner(M)==True:
                print('spelare',(spelare + 1) % max_spelare, 'vann!')
                break
            
            
        
main()
















