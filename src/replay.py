# Importing Libraries
import os
import time

# Importing Custom Modules
from defs import *
from utils import Game
from spells import castSpell
from barbarian import spawnBarbarian
from king import King, attackKing

file = open('../history/replay.txt', 'r')
file = file.read()
file = file.split('\n')
numReplays = len(file) - 1

print("You have played " + str(numReplays) + " games.")
while(1):
    reqReplay = int(input("Enter the number of the replay you want to view(Latest game => 1 and 0 to quit): "))
    
    if(reqReplay == 0):
        break

    while(reqReplay <= 0 or reqReplay > numReplays):
        reqReplay = int(input("Please enter a valid input: "))

    replayStr = file[numReplays - reqReplay]

    # Initializing Game
    game = Game()
    moves = []

    for key in replayStr:
        # Printing Board
        os.system('clear')
        game.printBoard()

        # Handling Input
        if key == 'q':
            game.state = False
        elif key in ['1', '2', '3']:
            spawnBarbarian(game, int(key))
        elif key in ['w', 'a', 's', 'd']:
            King.move(game,key)
        elif key in ['r', 'h']:
            castSpell(game, key)
        elif key == ' ':
            attackKing(game)
            
        game.update()
        time.sleep(0.1)

    os.system('clear')
