

#==========================================
# Purpose: find the value of x^y
# Input Parameter(s): x: base number and y: exponent
# Return Value(s): prod
#=======================================
def expo(x,y):
    prod = 1
    i = 0
    while i < y:
        total = 0
        i += 1
        j = 0
        while j < x:
            total += prod
            j += 1
        prod = total
    return prod


#==========================================
# Purpose: Rock paper scissors game
# Input Parameter(s): none
# Return Value(s): 0, -1, or 1
#=======================================
import random

def rps_round():
    player_move = input("Enter R, P, or S:")
    while player_move != 'R' and player_move != 'P' and player_move != 'S':
        print('Invalid Input')
        player_move = input("Enter R, P, or S:")
    comp_move = random.choice('RPS')
    if comp_move == 'R' and player_move == 'P':
        print('Computer selects R')
        print('Player Wins!')
        return 1
    elif comp_move == 'R' and player_move == 'S':
        print('Computer selects R')
        print('Computer Wins!')
        return -1
    elif comp_move == 'P' and player_move == 'R':
        print('Computer selects P')
        print('Computer Wins!')
        return -1
    elif comp_move == 'P' and player_move == 'S':
        print('Computer selects P')
        print('Player Wins!')
        return 1
    elif comp_move == 'S' and player_move == 'P':
        print('Computer selects S')
        print('Computer Wins!')
        return -1
    elif comp_move == 'S' and player_move == 'R':
        print('Computer selects S')
        print('Player Wins!')
        return 1
    else:
        print('Computer selects',comp_move)
        print('Tie!')
        return 0


#==========================================
# Purpose: play multiple rounds of rps to a reach a choosen win number
# Input Parameter(s): num_wins: the number of times you need to win to end the program
# Return Value(s): x: the value assigned to determine if player or computer won
#==========================================
def rps_game(num_wins):
    i = 0
    j = 0
    while i < num_wins and j < num_wins:
       x = rps_round()
       if x == 1:
           i += 1
       elif x == -1:
           j += 1
    return x
