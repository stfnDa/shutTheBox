#spiel mit zwei würfeln und tafeln mit 1 - 9 man muss sie weg kriegen, die die man wegtut
#(eins oder mehr nach jedem wurf) müssen zusammen die würfel augen ergeben

import random
from time import sleep

#aktuelles brett printen
def latestBoard():
    for x in range(9):
        if board[x] == False:
            print("[]", end=" ")
        else:
            print(board[x], end=" ")
    print("")  

#würfeln
def Roll():
    dice = [1, 2, 3, 4, 5, 6]
    dice1 = random.choice(dice)
    dice2 = random.choice(dice)
    print("Your numbers are:", dice1, "and", dice2)
    dices = dice1 + dice2
    return dices

#überprüfen ob möglich TODO
def possible():
    game = False
    for x in range(9):
        if(board[x] != False):
            print(board[x])
    for x in range(9):
        if(board[x] != False):
            if(dices == board[x]):
                game = True
                

    for x in range (9):
        if(board[x] != False):
            if (dices > board[x]):
                without1 = dices - board[x]
                if(without1 != board[x]):
                    for y in range(9):
                        if(board[y] != False):
                            if(without1 == board[y]):
                                game = True
                
    return game





#aussuchen welcher wegkommen und überprüfen ob die so passen
def eliminate():
    anzahl = input("How many fields do you want to eliminate? 1 or 2: ")
    try:
        anzahl = int(anzahl)
    except ValueError:
        print("Enter a integer!")
        eliminate()
    field = [0, 0]
    fields = 0
    if anzahl > 0 and anzahl < 3:
        #welcher felder
        for x in range (anzahl):
            field[x] = int(input("Which field? (enter only one!): "))
            fields = fields + field[x] #felder zusammen addiert
        print(dices, fields)
        if (fields == dices):#passt
            print("Alright! Fields eliminated!")
            for x in range (anzahl):
                temp = field[x] - 1
                board[temp] = False
        else: #passt nicht
            print("Your chosen fields don't add up to your dices but it's possible! Try again!")
            eliminate()
    else:
        print("Enter a valid integer! Either 1, 2 or 3!")
        eliminate(int)

game = True
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

while game == True:
    latestBoard()
    sleep(1)
    dices = Roll()
    #TODO check if those numbers are still possible
    game = possible()
    sleep(1)
    if (game == True):
        eliminate()

sleep(20)        